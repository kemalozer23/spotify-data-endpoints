import requests
from access_token import Spotify


class Albums(Spotify):

    def __init__(self, CLIENT_ID=None, CLIENT_SECRET=None, BASE_URL='https://api.spotify.com/v1/'):
        super().__init__(CLIENT_ID, CLIENT_SECRET, BASE_URL)

    # Get Spotify catalog information for a single album.
    def get_album(self, id=None, **kwargs):
        album_data = requests.get(self.base_url + "albums/" + id, headers=self.headers).json()

        return album_data

    # Get Spotify catalog information for multiple albums identified by their Spotify IDs.
    def get_albums(self, ids=None, **kwargs):
        albums_data = requests.get(self.base_url + "albums?ids=" + ids, headers=self.headers).json()

        return albums_data

    # Get Spotify catalog information about an album’s tracks. 
    def get_album_tracks(self, id=None, **kwargs):   # Need to implement offset, market and limit to the query
        albums_tracks_data = requests.get(self.base_url + "albums/" + id + "/tracks", headers=self.headers).json()

        return albums_tracks_data

    # Get a list of new album releases featured in Spotify.
    def get_new_releases(self, **kwargs):
        new_releases = requests.get(self.base_url + "browse/new-releases", headers=self.headers).json()

        return new_releases