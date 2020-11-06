import os
from app import app, db
from flask import Flask, render_template, request, session, url_for, redirect, flash, get_flashed_messages
from flask_mail import Mail, Message
from app.models import User, Event, user_favorites
from tempfile import mkdtemp
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from datetime import datetime
import base64

# os.environ["APP_SETTINGS"] = "./config.cfg"
# mail = Mail(app)

#routes
@app.route("/", methods=['GET', 'POST'])
def home():
    if current_user.is_anonymous:
        return render_template("landing.html")
    else:
        events = Event.query.all()
        for event in events:
            event.img = base64.b64encode(event.img).decode('ascii')
        return render_template("home.html", title="Find Events", events=events)


#this one is just to handle not falling into the landing page over and over
@app.route("/index", methods=['GET', 'POST'])
def index():
    events = Event.query.all()
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
        #done this way and not with wtforms to preserve data binding in JS
        r = request.form
        img = request.files['img']
        name = r.get("name")
        event_type = r.get("type")
        periodicity = r.get("periodicity")
        period = r.get("period")
        location = r.get("location")
        date = r.get("date")
        starting_time = r.get("starting")

        link = r.get("link")
        organizer = r.get("organizer")
        organizer_web = r.get("web")
        description = r.get("description")
        #commit to the database
        event = Event(
            name=name,
            event_type=event_type,
            recurrence=periodicity,
            periodicity=period,
            location=location,
            date=datetime.strptime(date, '%Y-%m-%d'),
            starting_time=starting_time,
            link=link,
            organizer=organizer,
            organizer_web=organizer_web,
            description=description,
            img=img.read(),
            user_id=current_user.get_id())
        db.session.add(event)
        db.session.commit()
        return 'saved to database'


@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/edit")
def edit():
    return render_template("edit.html")

@app.route("/favorites")
def favorites():
    return render_template("favorites.html", title="Favorite Events")

@app.route("/my-events")
def my_events():
    return render_template("my-events.html", title="My Events") 

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


@app.route("/event")
def event():
    return render_template("event.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    session.init_app(app)

    app.run(debug=True)
