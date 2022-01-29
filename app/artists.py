import requests
from access_token import Spotify

class Artists(Spotify):

    def __init__(self, CLIENT_ID=None, CLIENT_SECRET=None, BASE_URL='https://api.spotify.com/v1/'):
        super().__init__(CLIENT_ID, CLIENT_SECRET, BASE_URL)

    def get_artist(self, id=None):
        
        artist_data = requests.get(self.base_url + "artists/" + id, headers=self.headers).json()

        return artist_data

    def get_artists(self, ids=None):
        
        artists_data = requests.get(self.base_url + "artists?ids=" + ids, headers=self.headers).json()

        return artists_data

    def get_artists_album(self, id=None, limit=None, market=None, offset=None):
        artists_albums = requests.get(self.base_url + "artists/" + id + "/albums", headers=self.headers).json()

        return artists_albums

    def get_artists_top_tracks(self, id=None, market=None):
        
        artists_top_tracks = requests.get(self.base_url + "artists/" + id + "/top-tracks?market=" + market, headers=self.headers).json()

        return artists_top_tracks

    def get_related_artists(self, id=None):
        
        related_artists = requests.get(self.base_url + "artists/" + id + "/related-artists", headers=self.headers).json()

        return related_artists