from flask import render_template, flash, redirect, url_for, session
from app import app # from __init__.py
from app import db # from __init__.py
from app.forms import LoginForm
from app.forms import CourseForm
from app.forms import RegistrationForm
from app.forms import FriendsForm
from app.models import User
from app.models import Post
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.models import User, Post


@app.route('/', methods=["GET" ,"POST"])
@app.route('/index', methods=["GET" ,"POST"])
@login_required
def index():

    form = CourseForm()
    update_course = User.query.filter_by(id=current_user.id).first()
    update_course.student_courses = form.student_courses.data
    db.session.commit()
    flash('Looking for students with the same course')
    found_buddy = User.query.filter_by(student_courses=update_course.student_courses)
    return render_template('index.html', title='User_Home', form=form, found_buddy=found_buddy)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # look at first result first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) # https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data) # need something like this for student column of courses
        user.set_password(form.password.data)
        post = Post(body=form.username.data )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/profile', methods=["Get", "POST"])
@login_required
def profilePage():
    image_file = url_for('static', filename = 'prof/' + current_user.image_file)
    #user = User.query.filter_by(username = current_user.username)
    return render_template("profile.html", title ='Profile', image_file=image_file )
