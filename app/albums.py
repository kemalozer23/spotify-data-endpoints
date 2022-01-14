import requests
import access_token
from access_token import Spotify

class Albums(Spotify):

    def __init__(self, CLIENT_ID=None, CLIENT_SECRET=None, BASE_URL = 'https://api.spotify.com/v1/'):
        super().__init__(CLIENT_ID=CLIENT_ID, CLIENT_SECRET=CLIENT_SECRET)
        self.base_url = BASE_URL
        self.headers = {
        "Authorization": f"Bearer {self.get_access_token()}"
        }

    def get_album(self, id=None, market=None):
        album_data = requests.get(self.base_url + "albums/" + id, headers=self.headers).json()

        return album_data

    def get_several_albums(self, ids=None, market=None):
        several_albums_data = requests.get(self.base_url + "albums?ids=" + ids, headers=self.headers).json()

        return several_albums_data

    def get_album_tracks(self, id=None, limit=None, market=None, offset=None): 
        albums_tracks_data = requests.get(self.base_url + "albums/" + id + "/tracks", headers=self.headers).json()

        return albums_tracks_data

    def get_saved_albums(self, limit=None, market=None, offset=None):
        saved_albums_data = requests.get(self.base_url + "me/albums", headers=self.headers).json()

        return saved_albums_data

    def save_albums(self, ids=None): 
        requests.put(self.base_url + "me/albums?ids=" + ids, headers=self.headers)

    def remove_albums(self, ids=None):
        requests.delete(self.base_url + "me/albums?ids=" + ids, headers=self.headers)

    def check_saved_albums(self, ids=None):
        does_contain = requests.get(self.base_url + "me/albums/contains?ids=" + ids, headers=self.headers).json()

        return does_contain

    def get_new_releases(self, country=None, limit=None, offset=None):
        new_releases = requests.get(self.base_url + "browse/new-releases", headers=self.headers).json()

        return new_releases