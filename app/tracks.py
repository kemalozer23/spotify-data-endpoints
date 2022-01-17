import requests
from access_token import Spotify

class Tracks(Spotify):

    def __init__(self, CLIENT_ID=None, CLIENT_SECRET=None, BASE_URL='https://api.spotify.com/v1/'):
        super().__init__(CLIENT_ID, CLIENT_SECRET, BASE_URL)

    def get_track(self, id=None, market=None):
        track_data = requests.get(self.base_url + "tracks/" + id, headers=self.headers).json()

        return track_data

    def get_tracks(self, ids=None, market=None):
        tracks_data = requests.get(self.base_url + "tracks?ids=" + ids, headers=self.headers).json()

        return tracks_data

    def get_saved_tracks(self, limit=None, market=None, offset=None):
        saved_tracks = requests.get(self.base_url + "me/tracks", headers=self.headers).json()

        return saved_tracks

    def get_audio_features(self, id=None):
        audio_features = requests.get(self.base_url + "audio-features/" + id, headers=self.headers).json()

        return audio_features

    def get_several_audio_features(self, ids=None):
        severeal_audio_features = requests.get(self.base_url + "audio-features?ids=" + ids, headers=self.headers).json()

        return severeal_audio_features

    def get_audio_analysis(self, id=None):
        audio_analysis = requests.get(self.base_url + "audio-analysis/" + id, headers=self.headers).json()

        return audio_analysis