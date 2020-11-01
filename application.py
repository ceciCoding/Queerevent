from flask import Flask, render_template, request, session, url_for, redirect
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from helpers import login_required

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#configure SQLite database with SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queerevent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    hash = db.Column(db.String(100), nullable=False)
    
    img = db.Relationship('UserImage', backref='user', uselist=False)
    events = db.Relationship('Event', backref='user')

#association table for favorite events
user_favorites = db.Table('user_favorites',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(10), nullable=False)
    recurrence = db.Column(db.String(10), nullable=False)
    periodicity = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    location = db.Column(db.String(150))
    starting_time = db.Column(db.DateTime)
    ending_time = db.Column(db.DateTime)
    organizer = db.Column(db.Strig(50))
    organizer_web = db.Column(db.String(150))
    link = db.Column(db.String(150))
    description = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    img = db.Relationship('EventImage', backref="Event", uselist=False)
    

class UserImage(bd.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class EventImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

#routes
@app.route("/")
def home():
    return render_template("home.html", title="Find Events")

@app.route("/landing.html")
def landing():
    return render_template("landing.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/create-account.html")
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
    app.run(debug=True)
