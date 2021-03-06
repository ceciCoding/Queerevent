from app import app, db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

#association table for favorite events
user_favorites = db.Table('user_favorites',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                          )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    pswd_hash = db.Column(db.String(300), nullable=False)
    img = db.Column(db.LargeBinary)
    events = db.relationship('Event', backref='user')
    favorites = db.relationship('Event', secondary=user_favorites, backref=db.backref('fans', lazy='dynamic'))

    def set_password(self, password):
        self.pswd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pswd_hash, password)



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(10), nullable=False)
    recurrence = db.Column(db.String(10), nullable=False)
    periodicity = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    location = db.Column(db.String(150))
    starting_time = db.Column(db.String(50))
    organizer = db.Column(db.String(50))
    organizer_web = db.Column(db.String(150))
    link = db.Column(db.String(150))
    description = db.Column(db.Text, nullable=False)
    img = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
