# Steps to run the application
* Python version used to code the application: Python 3.7.3
1. Change your working directory to Assessment-VisualBI
2. Install all the dependencies using the following command
    ```code
    pip install -r requirements.txt
    ```
3. Launch the application using the following command
    ```code
    python launch.py
    ```
* For POST request we need to pass token in the query string, ex:
    ```url
    /api/v1/albums/?token=<token_value>
    ```
* The token can be generated from the home ('/') page once you login
* Existing user credentials:
    ```
    username = admin
    password = qwerty@12345
    ```
# API Information
| Method | Route | Description |
| ------ | ------ | ------ |
| GET | /api/v1/albums/ | returns list of albums containg list of related songs |
| GET | /api/v1/albums/<album_id> | returns a album matching the id passed |
| GET | /api/v1/songs/ | returns list of songs with album and artist details |
| POST | /api/v1/albums/ | create albums(s) |
| POST | /api/v1/songs/ | create sonsg(s) |
| POST | /api/v1/artists/ | create artist(s) |
Below are the sample responses for GET requests and sample body for POST requests.
#### Sample reponse for /api/v1/albums/
```json
[
    {
        "album_id": 1,
        "album_title": "Wonder",
        "artist": "Shawn Mendes",
        "songs": [
            {
                "seconds": 300,
                "song_title": "Wonder"
            },
            {
                "seconds": 300,
                "song_title": "Higher"
            },
            {
                "seconds": 300,
                "song_title": "24 Hours"
            }
        ]
    }
]
```
#### Sample reponse for /api/v1/albums/1
```json
{
    "album_id": [
        1
    ],
    "album_title": [
        "Wonder"
    ],
    "artist": [
        "Shawn Mendes"
    ],
    "songs": [
        {
            "seconds": 300,
            "song_title": "Wonder"
        },
        {
            "seconds": 300,
            "song_title": "Higher"
        }
    ]
}
```
#### Sample reponse for /api/v1/songs/
```json
[
    {
        "album_id": 1,
        "album_title": "Wonder",
        "artist": "Shawn Mendes",
        "seconds": 300,
        "song_id": 1,
        "song_title": "Wonder",
        "thumbnail_url": "https://homepages.cae.wisc.edu/~ece533/images/tulips.png"
    },
    {
        "album_id": 1,
        "album_title": "Wonder",
        "artist": "Shawn Mendes",
        "seconds": 300,
        "song_id": 2,
        "song_title": "Higher",
        "thumbnail_url": "https://homepages.cae.wisc.edu/~ece533/images/tulips.png"
    }
]
```
#### Sample JSON body to create album(s)
```json
[
    {
        "album_id": 8,
        "album_title": "test",
        "artist_id": 2
    },
    {
        "album_id": 9,
        "album_title": "test-test",
        "artist_id": 2
    }
]
```
#### Sample JSON body to create song(s)
```json
[
    {
        "song_id" : 55,
        "song_title" : "test song",
        "seconds" : "450",
        "thumbnail_url" : "www.test-url.com/image.png",
        "album_id" : 4
    }
]
```
#### Sample JSON body to create artist(s)
```json
[
    {
        "artist_id": 3,
        "artist":"singer"
    }
]
```