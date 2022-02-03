from albums import AlbumsTables
from artists import ArtistsTables
from tracks import TracksTables

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

import streamlit as st

alchemist_albums = AlbumsTables()
alchemist_artists = ArtistsTables()
alchemist_tracks = TracksTables()

ARTIST_ID = "0eVyjRhzZKke2KFYTcDkeu"

CYCLES = "34R4rwCqNDxQpttZfCT0Wn"
SUPER_TECMO_BO = "5leBUcbk6qAb5cDHYuVwBO"
THIS_THING_OF_OURS_2 = "0bFVjwPABfPBSWimES0TJ6"
BO_JACKSON = "1KHFw3hsKvNGGCkXKQMrbT"
COVERT_COUP = "7zAHNpdTeq8jNCmZaGK3jf"
THIS_THING_OF_OURS = "44qqs0b21hn7gAsuTioQkT"
HARAM = "0RPanQrJXRyTJoiq2trm7k"
CARRY_THE_FIRE = "61824hWgdxWH4Gtjk3BBoP"
THE_FOOD_VILLAIN = "7AodQt6yKbtY1MBGfz5z4V"
A_DOCTOR_PAINTER = "3QNTSNrJN5H8eQ4Xet4qhZ"
ALFREDO = "3znl1qe13kyjQv7KcR685N"
LULU = "4cj3HwgA7wk89PJW8sMpDZ"
THE_PRICE_OF_TEA = "52yTF9qryiuTlSNqhHObgd"
LAMB_OVER_RICE = "3BPX4x5EQOd9vzpPC2rMrm"
YACHT_ROCK = "1IQmCioMTatFSX6biSISx5"
BREAD = "6HB5Nq7lSjvTs3gJom6BXI"
FETTI = "3JgtFZroTUGoklTtb2xOne"
LAUNCH_MEET = "4hFVrUV21optQlCdtr3RgR"
FANTASY_ISLAND = "4ODrSTpVEWcHAGuSKUY4vl"

ids = ",".join([CYCLES,
                SUPER_TECMO_BO,
                THIS_THING_OF_OURS_2,
                BO_JACKSON,
                COVERT_COUP,
                THIS_THING_OF_OURS,
                HARAM,
                CARRY_THE_FIRE,
                THE_FOOD_VILLAIN,
                A_DOCTOR_PAINTER,
                ALFREDO,
                LULU,
                THE_PRICE_OF_TEA,
                YACHT_ROCK,
                BREAD,
                FETTI,
                LAUNCH_MEET,
                FANTASY_ISLAND])


df = alchemist_albums.albums_table(ids=ids)
df_2 = alchemist_albums.album_tracks_table(id=ALFREDO)

fig = px.bar(df, x="names", y="total_tracks")

st.write(df_2)
# st.write(fig)

# df = alchemist_tracks.audio_analysis_table()