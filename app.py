import os
from flask import Flask, render_template, request, session, url_for, redirect
from flask_session import Session
from flask_mail import Mail, Message
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from helpers import login_required
from config import Config
from models import User, Event, UserImage, EventImage, user_favorites
#for future modifications of the db models
from flask_migrate import Migrate
from tempfile import mkdtemp
from flask_login import LoginManager, current_user, login_user, LoginForm, flash

app = Flask(__name__)
login = LoginManager(app)
app.debug = True

app.config.from_object(Config)
# app.config.from_envvar('APP_SETTINGS')
os.environ["APP_SETTINGS"] = "./config.cfg"

#email config
app.config['"MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
mail = Mail(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#configure SQLite database with SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///queerevent.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
            return redirect(url_for("home"))
    return render_template("login.html")


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
