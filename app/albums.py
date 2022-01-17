import requests
from access_token import Spotify

class Albums(Spotify):

    def __init__(self, CLIENT_ID=None, CLIENT_SECRET=None, BASE_URL='https://api.spotify.com/v1/'):
        super().__init__(CLIENT_ID, CLIENT_SECRET, BASE_URL)

    def get_album(self, id=None, market=None):
        album_data = requests.get(self.base_url + "albums/" + id, headers=self.headers).json()

        return album_data

    def get_albums(self, ids=None, market=None):
        albums_data = requests.get(self.base_url + "albums?ids=" + ids, headers=self.headers).json()

        return albums_data

    def get_album_tracks(self, id=None, limit=None, market=None, offset=None):   # Need implement offset, market and limit to the query
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