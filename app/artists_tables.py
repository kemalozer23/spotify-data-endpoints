from tkinter.font import names
import requests
from access_token import Spotify
from albums import Albums
from artists import Artists
from tracks import Tracks
import pandas as pd


class ArtistsTables(Artists):

    def __init__(self):
        super().__init__()

    # Create a dataframe using the get_artist function defined in the Artists class.
    def artist_table(self, id=None):

        artist_data = self.get_artist(id=id)

        df = pd.DataFrame({
            "Name": [artist_data["name"]],
            "Popularity": [artist_data["popularity"]],
            "Followers": [artist_data["followers"]["total"]]
        })

        return df

    # Create a dataframe using the get_artists function defined in the Artists class.
    def artists_table(self, ids=None):

        artists_data = self.get_artists(ids=ids)

        names = []
    
        for i in range(len(ids.split(","))):
            names.append(artists_data["artists"][i]["name"])

        df = pd.DataFrame({"Name": names})

        return df

    # Create a dataframe using the get_artists_top_tracks function defined in the Artists class.
    def top_tracks_table(self, id=None, market=None):
    
        top_tracks = self.get_artists_top_tracks(id=id, market=market)

        names = []
        popularity = []
        duration_ms = []
        album = []
        release_date = []

        for i in range(10):
            names.append(top_tracks["tracks"][i]["name"])
            popularity.append(top_tracks["tracks"][i]["popularity"])
            duration_ms.append(top_tracks["tracks"][i]["duration_ms"])
            album.append(top_tracks["tracks"][i]["album"]["name"])
            release_date.append(top_tracks["tracks"][i]["album"]["release_date"])

        df = pd.DataFrame({
            "name": names,
            "album": album,
            "release Date": release_date,
            "popularity": popularity, 
            "duration_ms": duration_ms
        })

        return df

    # Create a dataframe using the get_related_artists function defined in the Artists class.
    def related_artists_table(self, id=None):

        related_artists = self.get_related_artists(id=id)

        names = []

        for i in range(20):
            names.append(related_artists["artists"][i]["name"])

        df = pd.DataFrame({"Name": names})

        return df