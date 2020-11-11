import base64
from app.models import User, Event, user_favorites
from flask_login import current_user

def decodeImage(img):
    return base64.b64encode(img).decode('ascii')

def checkFavorites(event):
    return User.query.join(user_favorites).join(Event).filter(
        (user_favorites.c.user_id == current_user.id) & (user_favorites.c.event_id == event.id)).all()

def setEvents(events):
    for event in events:
        if checkFavorites(event):
            event.fan = True
        if event.img:
            event.image = decodeImage(event.img)
