from music_app.untilities import APIUtilities, GeneralUtilities
from flask import Blueprint, request

songs = Blueprint('songs', __name__)

# Create route to get all the songs in DB
@songs.route('/api/v1/songs/', methods=['GET'])
def get_all_songs():
    return APIUtilities.get_all_songs()

# Create route to create new song(s)
@songs.route('/api/v1/songs/', methods=['POST'])
@GeneralUtilities.token_required
def create_song():

    # Get the JSON from the requested posted to server
    data = request.get_json()
    return APIUtilities.create_song(data)