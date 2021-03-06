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
    phone =db.relationship('Phone', backref = 'author', lazy = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)

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
class Phone(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    phone_number = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,name,phone_number,user_id):
        self.name = name
        self.phone_number = phone_number
        self.user_id = user_id

    def __repr__(self):
        return f'The Avengers name is {self.name} \n and their phone number is {self.phone_numer}'