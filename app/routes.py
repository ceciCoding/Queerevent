import os
from app import app, db
from flask import Flask, render_template, request, session, url_for, redirect, flash, get_flashed_messages, jsonify, make_response
from flask_mail import Mail, Message
from app.models import User, Event, user_favorites
from tempfile import mkdtemp
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
from app.forms import LoginForm, RegistrationForm, EditForm
from werkzeug.urls import url_parse
from datetime import datetime
import geocoder
import base64

# os.environ["APP_SETTINGS"] = "./config.cfg"
# mail = Mail(app)

#routes
@app.route("/", methods=['GET', 'POST'])
def home():
    if current_user.is_anonymous:
        return render_template("landing.html")
    else:
        #search bar logic
        q = request.args.get("q")
        if q:
            events = Event.query.filter((Event.name.contains(q)))
            print(events)
            for event in events:
                user_is_fan = User.query.join(user_favorites).join(Event).filter(
                    (user_favorites.c.user_id == current_user.id) & (user_favorites.c.event_id == event.id)).all()
                if user_is_fan:
                    event.fan = True
                if event.img:
                    event.image = base64.b64encode(event.img).decode('ascii')
            return render_template("home.html", title="Find Events", events=events)
        else:
            events = Event.query.all()
            for event in events:
                user_is_fan = User.query.join(user_favorites).join(Event).filter(
                    (user_favorites.c.user_id == current_user.id) & (user_favorites.c.event_id == event.id)).all()
                if user_is_fan:
                    event.fan = True
                if event.img:
                    event.image = base64.b64encode(event.img).decode('ascii')
            return render_template("home.html", title="Find Events", events=events)


#this one is just to handle not falling into the landing page over and over
@app.route("/index", methods=['GET', 'POST'])
def index():
    events = Event.query.all()
    for event in events:
        if current_user.is_authenticated:
            user_is_fan = User.query.join(user_favorites).join(Event).filter(
                (user_favorites.c.user_id == current_user.id) & (user_favorites.c.event_id == event.id)).all()
        if event.img:
            event.image = base64.b64encode(event.img).decode('ascii')
    return render_template("home.html", title="Find Events", events=events)


@app.route("/login",  methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for('home'))
            else:
                flash("Invalid password")
                return render_template('login.html', form=form)
        else:
            flash("Invalid username")
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)
    
        
@app.route("/create-account", methods=["GET", "POST"])
def create():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("create-account.html", form=form)


@app.route("/logout")
def logout():
    logout_user();
    return redirect(url_for('index'))


@app.route("/new", methods=["GET", "POST"])
@login_required
def new_event():
    if request.method == 'GET':
        return render_template("new.html")
    else:
        #done this way and not with wtforms to preserve cool data binding in JS
        r = request.form
        img = request.files['img']
        name = r.get("name")
        event_type = r.get("type")
        periodicity = r.get("periodicity")
        if periodicity != 'Recurring':
            date = r.get("date")
            date = datetime.strptime(date, '%Y-%m-%d')
        else:
            date = None
        period = r.get("period")
        location = r.get("location")
        starting_time = r.get("starting")
        link = r.get("link")
        organizer = r.get("organizer")
        organizer_web = r.get("web")
        description = r.get("description")
        #check for errors in the selects
        EVENT_TYPES = ["Physical", "Online"]
        PERIODICITIES = ["One time", "Recurring"]
        if event_type not in EVENT_TYPES or periodicity not in PERIODICITIES:
            return render_template("new.html")
        #commit to the database
        event = Event(
            name=name,
            event_type=event_type,
            recurrence=periodicity,
            periodicity=period,
            location=location,
            starting_time=starting_time,
            link=link,
            organizer=organizer,
            organizer_web=organizer_web,
            description=description,
            img=img.read(),
            user_id=current_user.get_id())
        if date:
            event.date = date
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('event', id=event.id))


@app.route("/event/<id>", methods=["GET", "POST"])
def event(id):
    event = Event.query.filter_by(id=id).first()
    if request.method == "GET":
        if current_user.is_authenticated:
            user_is_fan = User.query.join(user_favorites).join(Event).filter(
                (user_favorites.c.user_id == current_user.id) & (user_favorites.c.event_id == event.id)).all()
        else:
            user_is_fan = False
        img = base64.b64encode(event.img).decode('ascii')
        if event.location:
            address = geocoder.google(
                event.location)
            coordinates = address.latlng
            print(coordinates)
        return render_template("event.html", event=event, img=img, user_is_fan=user_is_fan, coordinates=coordinates)
    else:
        db.session.delete(event)
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    if current_user.img:
        img = base64.b64encode(current_user.img).decode('ascii')
        return render_template("account.html", img=img)
    else:
        return render_template("account.html")


@app.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    form = EditForm()
    if request.method == "GET":
        if current_user.img:
            img = base64.b64encode(current_user.img).decode('ascii')
        else:
            img = None
        return render_template("edit.html", form=form, img=img)
    else:
        img = request.files["change"]
        if form.validate_on_submit():
            if form.name.data:
                current_user.name = form.name.data
            if form.new_password.data:
                if current_user.check_password(form.old_password.data):
                    current_user.set_password(form.new_password.data)
            if img:
                current_user.img = img.read()
            db.session.commit()
            return redirect(url_for("account"))
        if img:
            current_user.img = img.read()
            db.session.commit()
            return redirect(url_for("account"))
        return redirect(url_for('account'))

@app.route("/favorites")
@login_required
def favorites():
    events = Event.query.join(user_favorites).join(User).filter(
            (user_favorites.c.user_id == current_user.id)).all()
    print(events)
    for event in events:
        if event.img:
            event.image = base64.b64encode(event.img).decode('ascii')
        event.fan = True
    return render_template("favorites.html", title="Favorite Events", events=events)

@app.route("/my-events")
@login_required
def my_events():
    events = Event.query.filter_by(user_id=current_user.id).all()
    for event in events:
        if event.img:
            event.image = base64.b64encode(event.img).decode('ascii')
        user_is_fan = Event.query.join(user_favorites).join(User).filter(
            (user_favorites.c.user_id == current_user.id) & (user_favorites.c.event_id == event.id)).first()
        if user_is_fan:
            event.fan = True
    return render_template("my-events.html", title="My Events", events=events) 

 
@app.route("/calendar")
@login_required
def calendar():
    return render_template("calendar.html")


@app.route("/toggle-favorite", methods=["POST"])
@login_required
def toggle_favorite():
    req = request.get_json()
    event = Event.query.filter_by(id=req["event"]).first()
    user_is_fan = User.query.join(user_favorites).join(Event).filter(
        (user_favorites.c.user_id == current_user.id) & (user_favorites.c.event_id == event.id)).all()
    if user_is_fan:
        event.fan = False
        event.fans.remove(current_user)
    else:
        event.fan = True
        event.fans.append(current_user)
    db.session.commit()
    res = make_response(jsonify(event.fan), 200)
    return res


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    session.init_app(app)

    app.run(debug=True)
