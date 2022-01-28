import requests
from access_token import Spotify
from albums import Albums
from artists import Artists
from tracks import Tracks
import pandas as pd

gramsa = Artists()

def top_tracks_table(id=None, market=None):
    top_tracks = gramsa.get_artists_top_tracks(id=id, market=market)

    top_tracks_list = []

    for i in range(10):
        top_tracks_list.append(top_tracks["tracks"][i]["name"])

    df = pd.DataFrame(data=top_tracks_list, columns=["Tracks"])

    return df


