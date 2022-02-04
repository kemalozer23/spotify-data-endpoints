import requests


class Spotify():
    
    CLIENT_ID = "testt"
    CLIENT_SECRET = ""
    BASE_URL = "https://api.spotify.com/v1/"
    AUTH_URL="https://accounts.spotify.com/api/token"


    def __init__(self):
        self.headers = {
        "Authorization": f"Bearer {self.get_access_token()}"
        }

    def get_access_token(self):
        
        # POST request
        auth_response = requests.post(self.AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': self.CLIENT_ID,
        'client_secret': self.CLIENT_SECRET,
        })

        # convert to JSON
        auth_response_data = auth_response.json()

        # save the access token
        access_token = auth_response_data['access_token']

        return access_token     