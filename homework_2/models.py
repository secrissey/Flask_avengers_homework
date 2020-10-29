from homework_2 import app, db, login_manager

# Import all fo the Werkzeug Security methods
from werkzeug.security import generate_password_hash, check_password_hash

# Import for DateTime Module (This comes from python)
from datetime import datetime

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False, unique = True)
    phone = db.Column(db.String(100), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship('post', backref = 'author', lazy = True)

    def __init__(self,name,phone,email,password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        """ Grab the password that is passed into the method, return the hashed
         version of the password which will be stored inside the database """

        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.name} has been created with the following email:{self.email}'


# Creation of the Post Model
# The Post model will have: id,title,content,date_created,user_id
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'The title of the post is {self.title} \n and the content is {self.content}'