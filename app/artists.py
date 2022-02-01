import requests
from access_token import Spotify


class Artists(Spotify):

    def __init__(self, CLIENT_ID=None, CLIENT_SECRET=None, BASE_URL='https://api.spotify.com/v1/'):
        super().__init__(CLIENT_ID, CLIENT_SECRET, BASE_URL)

    # Get Spotify catalog information for a single artist identified by their unique Spotify ID. 
    def get_artist(self, id=None, **kwargs):
        
        artist_data = requests.get(self.base_url + "artists/" + id, headers=self.headers).json()

        return artist_data

    # Get Spotify catalog information for several artists based on their Spotify IDs.
    def get_artists(self, ids=None, **kwargs):
        
        artists_data = requests.get(self.base_url + "artists?ids=" + ids, headers=self.headers).json()

        return artists_data

    # Get Spotify catalog information about an artist's albums.
    def get_artists_album(self, id=None, **kwargs):
        artists_albums = requests.get(self.base_url + "artists/" + id + "/albums", headers=self.headers).json()

        return artists_albums

    # Get Spotify catalog information about an artist's top tracks by country.
    def get_artists_top_tracks(self, id=None, market=None, **kwargs):
        
        artists_top_tracks = requests.get(self.base_url + "artists/" + id + "/top-tracks?market=" + market, headers=self.headers).json()

        return artists_top_tracks

    # Get Spotify catalog information about artists similar to a given artist.
    def get_related_artists(self, id=None, **kwargs):
        
        related_artists = requests.get(self.base_url + "artists/" + id + "/related-artists", headers=self.headers).json()

        return related_artists