import os
from app import app
from flask import Flask, render_template, request, session, url_for, redirect, flash, get_flashed_messages
from flask_mail import Mail, Message
from app.models import User, Event, UserImage, EventImage, user_favorites
from tempfile import mkdtemp
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from app.forms import LoginForm

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
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid user email or password')
            return redirect(url_for("login"), form=form)
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/create-account.html", methods=["GET", "POST"])
def create():
    return render_template("create-account.html")


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
