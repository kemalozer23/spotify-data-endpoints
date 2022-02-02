import requests
from access_token import Spotify
from albums import Albums
from artists import Artists
from tracks import Tracks
import pandas as pd


class TracksTables(Tracks):

    def __init__(self):
        super().__init__()

    def audio_features_table(self, id=None):

        audio_features = self.get_audio_features(id=id)

        df = pd.DataFrame({
            "id": audio_features["id"],
            "Acousticness": audio_features["acousticness"],
            "Danceability": audio_features["danceability"],
            "Duration_ms": audio_features["duration_ms"],
            "Energy": audio_features["energy"],
            "Instrumentalness": audio_features["instrumentalness"],
            "Key": audio_features["key"],
            "Liveness": audio_features["liveness"],
            "Loudness": audio_features["loudness"],
            "Mode": audio_features["mode"],
            "Speechiness": audio_features["speechiness"],
            "Tempo": audio_features["tempo"],
            "Time_signature": audio_features["time_signature"],
            "Valence": audio_features["valence"]
        }, index=[0])

        return df

    def several_audio_features_table(self, ids=None):

        severeal_audio_features = self.get_several_audio_features(ids=ids)

        id = []
        acousticness = []
        danceability = []
        duration_ms = []
        energy = []
        instrumentalness = []
        key = []
        liveness = []
        loudness = []
        mode = []
        speechiness = []
        tempo = []
        time_signature = []
        valence = []

        for i in range(len(ids.split(","))):
            id.append(severeal_audio_features["audio_features"][i]["id"])
            acousticness.append(severeal_audio_features["audio_features"][i]["acousticness"])
            danceability.append(severeal_audio_features["audio_features"][i]["danceability"])
            duration_ms.append(severeal_audio_features["audio_features"][i]["duration_ms"])
            energy.append(severeal_audio_features["audio_features"][i]["energy"])
            instrumentalness.append(severeal_audio_features["audio_features"][i]["instrumentalness"])
            key.append(severeal_audio_features["audio_features"][i]["key"])
            liveness.append(severeal_audio_features["audio_features"][i]["liveness"])
            loudness.append(severeal_audio_features["audio_features"][i]["loudness"])
            mode.append(severeal_audio_features["audio_features"][i]["mode"])
            speechiness.append(severeal_audio_features["audio_features"][i]["speechiness"])
            tempo.append(severeal_audio_features["audio_features"][i]["tempo"])
            time_signature.append(severeal_audio_features["audio_features"][i]["time_signature"])
            valence.append(severeal_audio_features["audio_features"][i]["valence"])

        df = pd.DataFrame({
            "id": id,
            "Acousticness": acousticness,
            "Danceability": danceability,
            "Duration_ms": duration_ms,
            "Energy": energy,
            "Instrumentalness": instrumentalness,
            "Key": key,
            "Liveness": liveness,
            "Loudness": loudness,
            "Mode": mode,
            "Speechiness": speechiness,
            "Tempo": tempo,
            "Time_signature": time_signature,
            "Valence": valence
        })

        return df

    def audio_analysis_table(self, id=None):

        audio_analysis = self.get_audio_analysis(id=id)

        # df = pd.DataFrame({
        # a lot of data 
        # })

        return audio_analysis