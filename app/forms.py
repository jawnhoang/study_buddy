from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from app.models import Post

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    course = StringField('What are you studying?', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username taken. Please use a different name.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email taken. Please use a different email.')


class CourseForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    student_courses = StringField('Courses interested in', validators=[DataRequired()])
    submit = SubmitField('Search')


class profileForm(FlaskForm):
    name = StringField('Update Username')
    picture = FileField('Update Picture', validators=[FileAllowed(['jpeg', 'jpg', 'png'])])
    course = StringField('Update Course')
    submit = SubmitField('Update Account')


    def __init__(self, oldName, *args, **kwargs): #initializes current name to user
        super(profileForm, self).__init__(*args, **kwargs)
        self.oldName = oldName

    def validate_name(self, username): #checks to see if name entered already exists
        newName = User.query.filter_by(username=self.name.data).first()
        if newName is not None:
            raise ValidationError('Username taken. Please use a different name.')
