from music_app import db

class Songs(db.Model):
    """
    A class to map the songs table using SQLAlchemy

    ...

    Attributes
    -------
    song_id     : Integer database column
        Holds the id of the song
    song_title  : String databse column
        Holds the song name
    seconds     : String databse column
        Holds the duration in seconds
    thumbnail_url: String databse column
        Holds the thumbnail url for song
    album_id    : Integer database column
        Holds the foreign key for albums table
    
    Methods
    -------
    __repr__()
        Method to represent the class object
    """
    song_id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(60), nullable=False)
    seconds = db.Column(db.Integer, nullable=False)
    thumbnail_url = db.Column(db.String(200), default='thumbnail.png')
    album_id = db.Column(db.Integer, db.ForeignKey('albums.album_id'), nullable=False)

    def __repr__(self):
        return f"Songs('{self.song_title}', '{self.seconds}', {self.album_id})"