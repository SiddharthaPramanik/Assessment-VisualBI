from music_app.untilities import APIUtilities, GeneralUtilities
from flask import Blueprint, request

albums = Blueprint('albums', __name__)

# Create route to get all the albums
@albums.route('/api/v1/albums/', methods=['GET'])
def get_all_albums():
    return APIUtilities.get_all_albums()

# Create route to get the album by the album_id passed
@albums.route('/api/v1/albums/<int:album_id>', methods=['GET'])
def get_album_by_id(album_id):
    return APIUtilities.get_album_by_id(album_id)

#Create route to create new album(s)
@albums.route('/api/v1/albums/', methods=['POST'])
@GeneralUtilities.token_required
def create_album():

    # Get the JSON from the requested posted to server
    data = request.get_json()
    return APIUtilities.create_album(data)