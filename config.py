# import the os module
import os

# Creation of base directory for application
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents\chicodes_sept2020\week_5\in_class


# Config Class
# Configure the database(when we have one) AND configure the SECRET KEY for the encryption of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this....'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False