from datetime import datetime
from app import db # comes from __init__ in the app folder
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model): # tables are made by making classes, inorder to do so we need to inheirt db.Model from sqlAlchemy
    id = db.Column(db.Integer, primary_key=True) # an integer that's going to be incremented everytime you add something to the db
    username = db.Column(db.String(64), index=True, unique=True) # index=true is a type of optimization, usernames have to be unique
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    student_courses = db.Column(db.String(64), index=True, unique=False)
    image_file = db.Column(db.String(64), nullable=False, default = 'default.jpeg')
    posts = db.relationship('Post', backref='author', lazy='dynamic') # lazy allows us to do operations a lot easier



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):                     # when you want to print out the user
        return '<User {}>'.format(self.username)

class Post(db.Model):  # how do we use this?
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256)) #saved usernames of all registered acc
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))       # for identifying who this user belongs to, foreign key(camelcase/lowercase)


    def __repr__(self):
        return '<Posts {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

'''
post2 = Post(body = "kid1")
post3 = Post(body="account3")
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.commit()'''
'''
db.create_all()
user1 = User(username='kid1', email="email@email.com")
user2 = User(password_hash='account3', email ="test@test1.com")
user3 = User(p='test54', email= "root@root.com")
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.commit()'''
"""
from app import db
from app.models import User, Post
db.create_all()
u = User(username = 'Carlos', email='carlos@example.com')
db.session.add(u)
db.session.commit()
u = User(username = 'Sam', email='sam@example.com')
db.session.add(u)
db.session.commit()
users = User.query.all()   gives us all the users
for user in users:
    print(user.id, user.username, user.email)
"""
