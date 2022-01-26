import requests
from access_token import Spotify
from albums import Albums
from artists import Artists
from tracks import Tracks

gramsa = Albums(CLIENT_ID="521227c9e92947dcaffe328f28b0b6e6", CLIENT_SECRET="b6f7c7c8f1ff4bb7b3489120c2557aa6")

print(gramsa.get_album(id="51heTwkSfb4Z5dRIgwU2bd"))