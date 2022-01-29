import requests
from access_token import Spotify
from albums import Albums
from artists import Artists
from tracks import Tracks
import pandas as pd

gramsa = Artists(CLIENT_ID=None, CLIENT_SECRET=None)

def artist_table(id=None):

    artist_data = gramsa.get_artist(id=id)

    df = pd.DataFrame({
        "Name": [artist_data["name"]],
        "Popularity": [artist_data["popularity"]],
        "Followers": [artist_data["followers"]["total"]]
    })

    return df

def artists_table(ids=None):

    artists_data = gramsa.get_artists(ids=ids)

    names = []
    
    for i in range(len(ids.split(","))):
        names.append(artists_data["artists"][i]["name"])

    df = pd.DataFrame({"Name": names})

    return df

def top_tracks_table(id=None, market=None):
    
    top_tracks = gramsa.get_artists_top_tracks(id=id, market=market)

    top_tracks_list = []
    artist_name = []
    duration_ms = []
    album = []
    release_date = []

    for i in range(10):
        top_tracks_list.append(top_tracks["tracks"][i]["name"])
        artist_name.append(top_tracks["tracks"][i]["popularity"])
        duration_ms.append(top_tracks["tracks"][i]["duration_ms"])
        album.append(top_tracks["tracks"][i]["album"]["name"])
        release_date.append(top_tracks["tracks"][i]["album"]["release_date"])

    df = pd.DataFrame({
        "Track": top_tracks_list,
        "Album": album,
        "Release Date": release_date,
        "Popularity": artist_name, 
        "Duration_ms": duration_ms
    })

    return df

def related_artists_table(id=None):

    related_artists = gramsa.get_related_artists(id=id)

    names = []

    for i in range(20):
        names.append(related_artists["artists"][i]["name"])

    df = pd.DataFrame({"Name": names})

    return df