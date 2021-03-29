from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from music_app.users.models import Users


class RegistrationForm(FlaskForm):
    """
    A class to create WT From for registeraion process

    ...

    Attributes
    -------
    username: StringFiled
        attribute to hold username once form is submitted
    email   : String databse column
        attribute to hold email once form is submitted
    password: String databse column
        attribute to hold password once form is submitted
    submit: SubmitField
        attribute to render a submit button
    confirm_password:
        attribute to hold confirm password once form is submitted
    
    Methods
    -------
    validate_username(username)
        Funtion to validate the username
    validate_email(email)
        Funtion to validate the email 
    """

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField('Comfirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """ Function to validate if the username is already in use """

        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken.')
    
    def validate_email(self, email):
        """ Function to validate if the email is already  registered """

        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already registered with us.')


class LoginForm(FlaskForm):
    """
    A class to create WT From for login

    ...

    Attributes
    -------
    username: StringFiled
        attribute to hold username once form is submitted
    password: String databse column
        attribute to hold password once form is submitted
    submit: SubmitField
        attribute to render a submit button
    remember: Boolean
        attribute to hold if user want to be remembered
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')