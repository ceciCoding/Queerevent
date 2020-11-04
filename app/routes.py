import os
from app import app, db
from flask import Flask, render_template, request, session, url_for, redirect, flash, get_flashed_messages
from flask_mail import Mail, Message
from app.models import User, Event, UserImage, EventImage, user_favorites
from tempfile import mkdtemp
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse

os.environ["APP_SETTINGS"] = "./config.cfg"

mail = Mail(app)

#routes
@app.route("/", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        return render_template("home.html")
    else:
        return render_template("landing.html")

@app.route("/login.html",  methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid user email or password')
            return redirect(url_for("login"), form=form)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return render_template("login.html", form=form)


@app.route("/create-account.html", methods=["GET", "POST"])
def create():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your are now registered')
        return redirect(url_for('login'))
    return render_template("create-account.html", form=form)


@app.route("/account.html")
def account():
    return render_template("account.html")

@app.route("/edit.html")
def edit():
    return render_template("edit.html")

@app.route("/favorites.html")
def favorites():
    return render_template("favorites.html", title="Favorite Events")

@app.route("/my-events.html")
def my_events():
    return render_template("my-events.html", title="My Events") 

@app.route("/calendar.html")
def calendar():
    return render_template("calendar.html")

@app.route("/new.html")
def new_event():
    return render_template("new.html")

@app.route("/event.html")
def event():
    return render_template("event.html")


if __name__ == "__main__":
    session.init_app(app)

    app.run(debug=True)
