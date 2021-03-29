from music_app.untilities import APIUtilities, GeneralUtilities
from flask import Blueprint, request

artists = Blueprint('artists', __name__)

# Create route to create new artist(s)
@artists.route('/api/v1/artists/', methods=['POST'])
@GeneralUtilities.token_required
def create_artist():

    # Get the JSON from the requested posted to server
    data = request.get_json()
    return APIUtilities.create_artist(data)