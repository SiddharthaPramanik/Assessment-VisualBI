from music_app import db
from music_app.albums.models import Albums

class Artists(db.Model):
    """
    A class to map the artists table using SQLAlchemy

    ...

    Attributes
    -------
    artist_id   : Integer database column
        Holds the id of the artist
    artist      : String databse column
        Holds the artist's name
    albums      : Relationship
        A relationship to albums table
    
    Methods
    -------
    __repr__()
        Method to represent the class object
    """
    artist_id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), nullable=False)
    albums = db.relationship('Albums', backref='albums', lazy=True)

    def __repr__(self):
        return f"Artists('{self.artist}')"