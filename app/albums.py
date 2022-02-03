from matplotlib import artist
import requests
from access_token import Spotify
import pandas as pd


class Albums(Spotify):

    def __init__(self):
        super().__init__()
    
    # Get Spotify catalog information for a single album.
    def get_album(self, id=None, **kwargs):
        album_data = requests.get(self.BASE_URL + "albums/" + id, headers=self.headers).json()

        return album_data

    # Get Spotify catalog information for multiple albums identified by their Spotify IDs.
    def get_albums(self, ids=None, **kwargs):
        albums_data = requests.get(self.BASE_URL + "albums?ids=" + ids, headers=self.headers).json()

        return albums_data

    # Get Spotify catalog information about an album’s tracks. 
    def get_album_tracks(self, id=None, **kwargs):   # Need to implement offset, market and limit to the query
        albums_tracks_data = requests.get(self.BASE_URL + "albums/" + id + "/tracks", headers=self.headers).json()

        return albums_tracks_data

    # Get a list of new album releases featured in Spotify.
    def get_new_releases(self, **kwargs):
        new_releases = requests.get(self.BASE_URL + "browse/new-releases", headers=self.headers).json()

        return new_releases


class AlbumsTables(Albums):

    def __init__(self):
        super().__init__()

    # Create a dataframe using the get_album function defined in the Albums class.
    def album_table(self, id=None):
        
        album_data = self.get_album(id=id)

        df = pd.DataFrame({
            "artists": album_data["artists"][0]["name"] + "," + album_data["artists"][1]["name"],
            "name": album_data["name"],
            "id": album_data["id"],
            "label": album_data["label"],
            "album_type": album_data["album_type"],
            "total_tracks": album_data["total_tracks"],
            "release_date": album_data["release_date"],
            "popularity": album_data["popularity"],
            "album_cover": album_data["images"][0]["url"]
        }, index=[0])

        return df

    # Create a dataframe using the get_albums function defined in the Albums class.
    def albums_table(self, ids=None):

        albums_data = self.get_albums(ids=ids)

        artists = []
        names = []
        album_type = []
        total_tracks = []
        release_date = []
        id = []
        album_covers = []
        label = []
        popularity = []

        for i in range(len(ids.split(","))):
            artists.append(albums_data["albums"][i]["artists"][0]["name"])
            names.append(albums_data["albums"][i]["name"])
            album_type.append(albums_data["albums"][i]["album_type"])
            total_tracks.append(albums_data["albums"][i]["total_tracks"])
            release_date.append(albums_data["albums"][i]["release_date"])
            id.append(albums_data["albums"][i]["id"])
            album_covers.append(albums_data["albums"][i]["images"][0]["url"])
            label.append(albums_data["albums"][i]["label"])
            popularity.append(albums_data["albums"][i]["popularity"])

        df = pd.DataFrame({
            "artists": artists,
            "names": names,
            "album_type": album_type,
            "total_tracks": total_tracks,
            "release_date": release_date,
            "id": id,
            "album_cover": album_covers,
            "label": label,
            "popularity": popularity
        })

        return df

    # Create a dataframe using the get_album_tracks function defined in the Albums class.
    def album_tracks_table(self, id=None):

        album_tracks_data = self.get_album_tracks(id=id)

        names = []
        duration_ms = []
        ids = []

        for i in range(album_tracks_data["total"]):
            names.append(album_tracks_data["items"][i]["name"])
            duration_ms.append(album_tracks_data["items"][i]["duration_ms"])
            ids.append(album_tracks_data["items"][i]["id"])

        df = pd.DataFrame({
            "names": names,
            "duration_ms": duration_ms,
            "id": ids
        })

        return df