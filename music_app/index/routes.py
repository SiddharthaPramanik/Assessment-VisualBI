from flask import Blueprint, render_template

index = Blueprint('index', __name__)

# Create a route for landing and home page
@index.route('/')
@index.route('/home/')
def home():
    return render_template('home.html', title='Home')