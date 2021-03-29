from music_app import db
from music_app.songs.models import Songs

class Albums(db.Model):
    """
    A class to map the artists table using SQLAlchemy

    ...

    Attributes
    -------
    album_id    : Integer database column
        Holds the id of the album
    album_title : String databse column
        Holds the albums's title
    artist_id   :
        Foreign key for artists table
    songs       : Relationship
        A relationship to songs table
    
    Methods
    -------
    __repr__()
        Method to represent the class object
    """
    album_id = db.Column(db.Integer, primary_key=True)
    album_title = db.Column(db.String(60), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.artist_id'), nullable=False)
    songs = db.relationship('Songs', backref='songs', lazy=True)

    def __repr__(self):
        return f"Albums('{self.album_title}', {self.artist_id})"