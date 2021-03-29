from music_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    """
    A class to map the users table using SQLAlchemy

    ...

    Attributes
    -------
    user_id : Integer database column
        Holds the id of the user from DB
    username: String databse column
        Holds the username for the user
    email   : String databse column
        Holds the email for the user
    password: String databse column
        Holds the hashed password for the user
    
    Methods
    -------
    get_id()
        Overwrites the get_id from db.Model class
    __repr__()
        Method to represent the class object
    """

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_id(self):
        return (self.user_id)
    
    def __repr__(self):
        return f"Users('{self.username}', '{self.email}')"