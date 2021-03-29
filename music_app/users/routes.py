import jwt
import datetime
from music_app.config import Config
from flask import Blueprint, redirect, render_template, request, url_for, flash
from music_app import bcrypt, db
from music_app.users.models import Users
from music_app.users.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

# Create blueprint for users
users = Blueprint('users', __name__)

# Create route for user login
@users.route('/login/', methods=['GET', 'POST'])
def login():

    # Check if the user is already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('index.home'))

    # Create an object of the login form and validate the entiry
    # on submission
    login_form = LoginForm()
    if login_form.validate_on_submit():

        # Validate the user password against the one storred in databse
        user = Users.query.filter_by(username=login_form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):

            # Log the user in and redirect to the page user was trying to access
            login_user(user=user, remember=login_form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index.home'))
        else:
            
            # On failure of authentication flash a message
            flash('Login Unsuccessful. Please check your username and password!', category='danger')
    
    # Render the login template if the method is not POST
    return render_template('login.html', title='Login', form=login_form)

# Create route to register a new user
@users.route('/register/', methods=['GET', 'POST'])
def register():

    # Check if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index.home'))

    # Create an object of the registeration form and validate the entiry
    # on submission
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():

        # Hash the password before we store it in database
        hashed_password = bcrypt.generate_password_hash(registration_form.password.data).decode('utf-8')

        # Create the user and add it to database
        user = Users(username=registration_form.username.data, email=registration_form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # Notify the user by a message and redirect to login page
        flash(f'{registration_form.username.data} has been registered!', category='success')
        return redirect(url_for('users.login'))
    
    return render_template('register.html', title='Register', form=registration_form)

# Create route for logging the user out
@users.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index.home'))

# Create route for new token creation for the user
@users.route('/token/')
@login_required
def token():

    # Use JWT to create a token by encodin the username with secret key
    token = jwt.encode({'username' : current_user.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=30)}, Config.SECRET_KEY, algorithm="HS256")
    return render_template('token.html', title='API Token', token=token)