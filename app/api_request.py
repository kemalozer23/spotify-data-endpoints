import requests

class Spotify():

    def __init__(self, CLIENT_ID="3142fa4bd991430b82404c2be96a7fcb", CLIENT_SECRET="8bf4cfb7ad2d4c15981ea65d863b72e7"):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET

    def get_access_token(self, AUTH_URL="https://accounts.spotify.com/api/token"):
        self.auth_url = AUTH_URL

        # POST request
        auth_response = requests.post(self.auth_url, {
        'grant_type': 'client_credentials',
        'client_id': self.client_id,
        'client_secret': self.client_secret,
        })

        # convert the response to JSON
        auth_response_data = auth_response.json()

        # save the access token
        access_token = auth_response_data['access_token']

        return access_token