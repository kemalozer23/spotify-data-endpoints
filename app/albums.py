import requests
import api_request
from api_request import Spotify

class Albums(Spotify):

    def __init__(self, CLIENT_ID="3142fa4bd991430b82404c2be96a7fcb", CLIENT_SECRET="8bf4cfb7ad2d4c15981ea65d863b72e7", BASE_URL = 'https://api.spotify.com/v1/'):
        super().__init__(CLIENT_ID=CLIENT_ID, CLIENT_SECRET=CLIENT_SECRET)
        self.base_url = BASE_URL
        self.headers = {
        'Authorization': f"Bearer {self.get_access_token()}"
        }

    def get_album(self, album_id=None):
        album_data = requests.get(self.base_url + "albums/" + album_id, headers=self.headers).json()
        
        return album_data

    def get_albums(self)