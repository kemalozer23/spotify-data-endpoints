import requests
from access_token import Spotify


class Artists(Spotify):

    def __init__(self):
        super().__init__()

    # Get Spotify catalog information for a single artist identified by their unique Spotify ID. 
    def get_artist(self, id=None, **kwargs):
        
        artist_data = requests.get(self.BASE_URL + "artists/" + id, headers=self.headers).json()

        return artist_data

    # Get Spotify catalog information for several artists based on their Spotify IDs.
    def get_artists(self, ids=None, **kwargs):
        
        artists_data = requests.get(self.BASE_URL + "artists?ids=" + ids, headers=self.headers).json()

        return artists_data

    # Get Spotify catalog information about an artist's albums.
    def get_artists_album(self, id=None, **kwargs):
        artists_albums = requests.get(self.BASE_URL + "artists/" + id + "/albums", headers=self.headers).json()

        return artists_albums

    # Get Spotify catalog information about an artist's top tracks by country.
    def get_artists_top_tracks(self, id=None, market=None, **kwargs):
        
        artists_top_tracks = requests.get(self.BASE_URL + "artists/" + id + "/top-tracks?market=" + market, headers=self.headers).json()

        return artists_top_tracks

    # Get Spotify catalog information about artists similar to a given artist.
    def get_related_artists(self, id=None, **kwargs):
        
        related_artists = requests.get(self.BASE_URL + "artists/" + id + "/related-artists", headers=self.headers).json()

        return related_artists