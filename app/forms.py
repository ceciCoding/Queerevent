from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TimeField, DateField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Event, EventImage, UserImage, user_favorites

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Invalid username')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password'), Length(min=8)])
    submit = SubmitField('Create Account')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email is already in use')


class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired(), Length(max=100)])
    event_type = SelectField('Type of Event', validators=[DataRequired()], choices=[('Online', 'Online'), ('Physical', 'Physical')])
    recurrence = SelectField('Periodicity', validators=[DataRequired()], choices=[('One time', 'One Time'), ('Recurring', 'Recurring')])
    periodicity = StringField('Periodicity', validators=[Length(max=50)])
    date = DateField('Date')
    location = StringField('Location', validators=[Length(max=150)])
    starting_time = TimeField('Starting Time')
    ending_time = TimeField('Ending Time')
    organizer = StringField('Organizer', validators=[Length(max=50)])
    organizer_web = StringField('Organizer\'s Website', validators=[Length(max=150)])
    link = StringField('Link to the Event', validators=[Length(max=150)])
    description = TextAreaField('Description', validators=[DataRequired()])
