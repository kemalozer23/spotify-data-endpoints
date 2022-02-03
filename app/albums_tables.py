import requests
from access_token import Spotify
from albums import Albums
from artists import Artists
from tracks import Tracks
import pandas as pd


class AlbumsTables(Albums):

    def __init__(self):
        super().__init__()

    # Create a dataframe using the get_album function defined in the Albums class.
    def album_table(self, id=None):
        
        album_data = self.get_album(id=id)

        df = pd.DataFrame({
            "artists": album_data["artists"][0]["name"],
            "name": album_data["name"],
            "album_type": album_data["album_type"],
            "total_tracks": album_data["total_tracks"],
            "release_date": album_data["release_date"]
        }, index=[0])

        album_cover = album_data["images"][0]["url"]

        return df

    # Create a dataframe using the get_albums function defined in the Albums class.
    def albums_table(self, ids=None):

        albums_data = self.get_albums(ids=ids)

        artists = []
        names = []
        album_type = []
        total_tracks = []
        release_date = []

        for i in range(len(ids.split(","))):
            artists.append(albums_data["albums"][i]["artists"][0]["name"])
            names.append(albums_data["albums"][i]["name"])
            album_type.append(albums_data["albums"][i]["album_type"])
            total_tracks.append(albums_data["albums"][i]["total_tracks"])
            release_date.append(albums_data["albums"][i]["release_date"])

        df = pd.DataFrame({
            "artists": artists,
            "names": names,
            "album_type": album_type,
            "total_tracks": total_tracks,
            "release_date": release_date
        })

        return df

    # Create a dataframe using the get_album_tracks function defined in the Albums class.
    def album_tracks_table(self, id=None):

        album_tracks_data = self.get_album_tracks(id=id)

        names = []
        duration_ms = []

        for i in range(album_tracks_data["total"]):
            names.append(album_tracks_data["items"][i]["name"])
            duration_ms.append(album_tracks_data["items"][i]["duration_ms"])

        df = pd.DataFrame({
            "names": names,
            "duration_ms": duration_ms
        })

        return df