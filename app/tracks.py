import requests
from access_token import Spotify


class Tracks(Spotify):

    def __init__(self):
        super().__init__()

    # Get Spotify catalog information for a single track identified by its unique Spotify ID.
    def get_track(self, id=None, market=None):
        
        if market==None:
            track_data = requests.get(self.BASE_URL + "tracks/" + id, headers=self.headers).json()
        else:
            track_data = requests.get(self.BASE_URL + "tracks/" + id + "?market=" + market, headers=self.headers).json()
        
        return track_data

    # Get Spotify catalog information for multiple tracks based on their Spotify IDs.
    def get_tracks(self, ids=None, **kwargs):
        
        tracks_data = requests.get(self.BASE_URL + "tracks?ids=" + ids, headers=self.headers).json()

        return tracks_data

    # Get audio feature information for a single track identified by its unique Spotify ID.
    def get_audio_features(self, id=None, **kwargs):
        
        audio_features = requests.get(self.BASE_URL + "audio-features/" + id, headers=self.headers).json()

        return audio_features

    # Get audio features for multiple tracks based on their Spotify IDs.
    def get_several_audio_features(self, ids=None, **kwargs):
        
        severeal_audio_features = requests.get(self.BASE_URL + "audio-features?ids=" + ids, headers=self.headers).json()

        return severeal_audio_features

    # Get an audio analysis for a track in the Spotify catalog.
    def get_audio_analysis(self, id=None, **kwargs):
        
        audio_analysis = requests.get(self.BASE_URL + "audio-analysis/" + id, headers=self.headers).json()

        return audio_analysis
    
    # Get a set of recommendations.
    def get_recommendations(self, seed_artists=None, seed_genres=None, seed_tracks=None, **kwargs):

        recommendations = requests.get(self.BASE_URL 
                                    + "recommendations?limit=10&market=US&" 
                                    + "seed_artists=" + seed_artists + "&" 
                                    + "seed_genres="+ seed_genres + "&" 
                                    + "seed_tracks=" + seed_tracks,
                                    headers=self.headers).json()

        return recommendations