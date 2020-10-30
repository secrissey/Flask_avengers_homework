# Import the app variable from the init
from homework_2 import app, db

# Import specific packages from flask
from flask import render_template,request, redirect, url_for

# Import Our Form(s)
from homework_2.forms import UserInfoForm, LoginForm, PhoneForm

# Import of our Model(s) for the Database
from homework_2.models import User, Phone, check_password_hash

# Import for Flask Login functions - login_required,login_user,current_user,logout_user
from flask_login import login_required,login_user,current_user,logout_user

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/avengers')
def testRoute():
    names = ['Flash','Thor','Black Widow','Maria Hill']
    return render_template('avengers.html',list_names = names)


# GET == Gathering Info
# POST == Sending Info
@app.route('/avengeregister', methods = ['GET','POST'])
def avengeregister():
    # Init our Form
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        name = form.name.data
        phone_number = form.phone_number.data
        email = form.email.data
        password = form.password.data
        #Print the data to the server that comes from the form
        print(name,phone_number,email,password)

        # Creation/Init of our User Class(aka Model)
        user = User(name,phone_number,email,password)

        # Open a connection to the database
        db.session.add(user)

        # Commit all data to the database
        db.session.commit()

    return render_template('avengeregister.html',user_form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        # saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        # check the password of the newly found user and 
        # validate the password against the hash value inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            # Redirect user
            return redirect(url_for('home'))
        else:
            # Redirect User to login route
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Creation of posts route(aka Crud Process)
@app.route('/phones', methods = ['GET', 'POST'])
@login_required
def phones():
    form = PhoneForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        phone_number = form.phone_number.data
        user_id = current_user.id
        phone = Phone(name,phone_number,user_id)

        db.session.add(phone)

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('phones.html', phone_form = form)

# post detail route to display info about a post
@app.route('/phones/<int:phone_id>')
@login_required
def phone_detail(phone_id):
    phone = Phone.query.get_or_404(phone_id)
    return render_template('phones_detail.html', phone = phone)

@app.route('/phone/update/<int:phone_id>', methods = ['GET', 'POST'])
@login_required
def phone_update(phone_id):
    phone = Phone.query.get_or_404(phone_id)
    form = PhoneForm()

    if request.method == 'POST' and form.validate():
        name = form.name.data
        phone_number = form.phone_number.data
        user_id = current_user.id

        # Update the Database with the new Info
        phone.name = name
        phone.phone_number = phone_number
        phone.user_id = user_id

        # Commit the changes to the Database
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('phone_update.html', update_form = form)

@app.route('/phones/delete/<int:phone_id>', methods = ['GET','POST','DELETE'])
@login_required
def phone_delete(phone_id):
    phone = Phone.query.get_or_404(phone_id)
    db.session.delete(phone)
    db.session.commit()
    return redirect(url_for('home'))       