import jwt
from functools import wraps
from music_app import db
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from music_app.config import Config
from music_app.songs.models import Songs
from music_app.albums.models import Albums
from music_app.artists.models import Artists

class APIUtilities(object):
    """
    A class used to contain all the methods calls for API

    ...

    Methods
    -------
    get_all_albums()
        Returns a JSON object containing all the albums
    get_all_songs()
        Returns a JSON object containing all the songs
    get_album_by_id(album_id)
        Returns a JSON object of an album matching album_id parameter
    create_album(data)
        Create a new album using the data parameter
    create_song(data)
        Create a new song using the data parameter
    create_artist(data)
        Create a new artist using the data parameter
    """

    def get_all_albums():
        """
        This function queries the albums table for all the
        albums present in it. It also lists the songs that
        are part of the album.
    
        :return:        Returns a JSON object with the data
        """

        # Empty list to hold the entire data
        data = []

        # Query the albums table to get all the existing albums
        albums = Albums.query.all()

        for album in albums:

            # Find the songs that are part of current album 
            songs_in_album = Songs.query.filter(
                Songs.album_id == album.album_id
            ).all()

            # Find the artists to whom the current album belong 
            artist = Artists.query.filter(
                Artists.artist_id == album.artist_id
            ).first()
    
            # Creat a dictionary to append to the data list
            data.append(
                {
                    'album_id': album.album_id,
                    'album_title': album.album_title,
                    'artist': artist.artist,
                    'songs':[
                        {
                            'song_title': song.song_title,
                            'seconds': song.seconds
                        }
                        for song in songs_in_album
                    ]
                }
            )

        # Return JSONified data
        return jsonify(data)
    
    def get_all_songs():
        """
        This function queries the songs table for all the
        songs present in it. It uses the relation between 
        songs and album as well as album and artist to
        return those information as well.
    
        :return:        Returns a JSON object with the data
        """

        data = []

        # Query the songs table to get all the existing song
        all_songs = Songs.query.all()
        
        for song in all_songs:

            # Find the album for the current song
            album = Albums.query.filter_by(
                album_id=song.album_id
            ).first()

            # Find the artist that the album for current song belongs to
            song_artist = Artists.query.filter(
                Artists.artist_id == album.artist_id
            ).first()

            # Creat a dictionary to append to the data list
            data.append(
                {
                    'song_id': song.song_id,
                    'song_title': song.song_title,
                    'seconds': song.seconds,
                    'thumbnail_url': song.thumbnail_url,
                    'album_id': song.album_id,
                    'album_title': album.album_title,
                    'artist': song_artist.artist
                }
            )

        return jsonify(data)

    def get_album_by_id(album_id):
        """
        This function queries the album table to find the album
        corrosponding to the album_id parameter passed.
    
        :param album_id:    id to search the album with
        :return:            Returns a JSON object with the data,
                            404 if album is not found
        """

        # Query the albums table and pick the first result
        album = Albums.query.filter_by(album_id=album_id).first()

        # Return 404 if the album don't exists
        if not album:
            return {'message' : 'No album found!'}, 404
        
        else:
            data = {}

            # Find the songs belonging to the album
            songs_in_album = Songs.query.filter(
                Songs.album_id == album.album_id
            ).all()

            # Find the artist that the album belongs to
            artist = Artists.query.filter(
                Artists.artist_id == album.artist_id
            ).first()

            # Add the data to a dictionary to return  
            data['album_id'] = album.album_id,
            data['album_title'] = album.album_title,
            data['artist'] = artist.artist,
            data['songs'] =[
                {
                    'song_title': song.song_title,
                    'seconds': song.seconds
                }
                for song in songs_in_album
            ]
            
            return jsonify(data)
    
    def create_album(data):
        """
        This function creates a new album(s) based on the 
        passed-in album data
    
        :param data:  JSONified list of albums data
        :return:        Success Message, 406 on album exists and 
                        if issue with the passed data
        """

        for album in data:
            try:
                # Query the albums table and pick the first result
                album_exists = Albums.query.filter_by(album_id=album["album_id"]).first()

                # Return 406 if the album already exists
                if  album_exists:
                    return {'message' : 'Album already exists'}, 406

                # Return 406 if the artist_id passed doesnot exist
                artist_exist = Artists.query.filter(
                        Artists.artist_id == album['artist_id']
                    ).first()
                if not artist_exist:
                    return {'message':f'The artist id: {album["artist_id"]} you are referring to doesnot exist. Please add the artist first.'}, 406
                
                # Create and add the album to the database
                new_album = Albums(album_id=album['album_id'], album_title=album['album_title'], artist_id=album['artist_id'])
                db.session.add(new_album)
                db.session.commit()

            except:
                return {'message': f'POST request failed for :{album} Please check your data and API link. '+\
                            'Albums after this instance, in the list, were not processed.'}, 406
        
        # Return a message that the albums are added
        return {'message' : f'New album(s) {[album["album_title"] for album in data]} created!'}
  
    def create_song(data):
        """
        This function creates new song(s) based on the 
        passed-in song data
    
        :param data:  JSONified list of songs data
        :return:        Success Message, 406 on song exists and 
                        if issue with the passed data
        """

        for song in data:
            try:
                # Query the songs table and pick the first result
                song_exists = Songs.query.filter_by(song_id=song["song_id"]).first()

                # Return 406 if the song already exists
                if  song_exists:
                    return {'message' : 'Song already exists'}, 406

                # Return 406 if the album_id passed doesnot exist
                album_exist = Albums.query.filter(
                        Albums.album_id == song['album_id']
                    ).first()
                if not album_exist:
                    return {'message':f'The album id: {song["album_id"]} you are referring to doesnot exist. Please add the album first.'}, 406
                
                # Create and add the song to the database
                new_song = Songs(song_id=song['song_id'], song_title=song['song_title'], seconds=song['seconds'], thumbnail_url=song['thumbnail_url'], album_id=song['album_id'])
                db.session.add(new_song)
                db.session.commit()

            except:
                return {'message': f'POST request failed for :{song} Please check your data and API link. '+\
                            'Albums after this instance, in the list, were not processed.'}, 406

        return {'message' : f'New song(s) {[song["song_title"] for song in data]} created!'}
    
    def create_artist(data):
        """
        This function creates new artist(s) based on the 
        passed-in artist data
    
        :param data:  JSONified list of songs data
        :return:        Success Message, 406 on artist exists and 
                        if issue with the passed data
        """

        for artist in data:
            try:
                # Query the artists table and pick the first result
                artist_exists = Artists.query.filter_by(artist_id=artist["artist_id"]).first()

                # Return 406 if the artist already exists
                if  artist_exists:
                    return {'message' : 'artist already exists'}, 406

                # Create and add the artist to the database
                new_artist = Artists(artist_id=artist['artist_id'], artist=artist['artist'])
                db.session.add(new_artist)
                db.session.commit()

            except:
                return {'message': f'POST request failed for :{artist} Please check your data and API link. '+\
                            'Albums after this instance, in the list, were not processed.'}, 406

        return {'message' : f'New artist(s) {[artist["artist"] for artist in data]} created!'}
    
class GeneralUtilities(object):
    """
    A class used to contain general purpose methods calls for the application

    ...

    Methods
    -------
    token_required()
        A decorator function to check for JWT token before executing a funtion
    """
    
    def token_required(func):
        """
        This is a decorator to check the presence and validity
        of a JWT token before calling the actual function
    
        :param func:    the function that is decorated with this
        :return:        return the function call on validation,
                        401 on missing/invalid token
        """
        @wraps(func)
        def decorated(*args, **kwargs):

            # Get the token from the query string
            token = request.args.get('token')

            # Return 401 is token is missing
            if not token:
                return jsonify({'message' : 'Token is missing!'}), 401

            # Try decoding the token
            try: 
                data = jwt.decode(token, Config.SECRET_KEY, algorithms="HS256")
            
            # Return 401 if the try block raises error
            except:
                return {'message' : 'Token is invalid!'}, 401

            return func(*args, **kwargs)
        return decorated
