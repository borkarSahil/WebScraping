SPOTIFY_CLIENT_ID_VAL = "5d00f5231e104028b1e83be3b3ef0286"
SPOTIFY_CLIENT_SECRET_VAL = "fe60b4120d6241afab5103ce712e4ed1"





import requests
from bs4 import BeautifulSoup

date = input("Which year top 100 songs do you wish to hear ? (YYYY-MM-DD) ")

URL = "https://www.billboard.com/charts/hot-100/"

# Scrapping data (titles) from URL  { START }

response = requests.get(URL + date)
website_html = response.text
# print(website_html)
soup = BeautifulSoup(website_html, "html.parser")

song_names_tag = soup.select("li ul li h3")
# print(song_names)
song_names = [song.getText().strip() for song in song_names_tag]
# print(song_names)

# Scrapping data (titles) from URL  { END }

# LOGIN IN SPOTIFY  {START}

from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = SPOTIFY_CLIENT_ID_VAL
SPOTIFY_CLIENT_SECRET = SPOTIFY_CLIENT_SECRET_VAL
URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=URI,
        scope="playlist-modify-private",
        username="demo")
    )

# print user playlist
# pprint(sp.current_user_playlists())

user = sp.current_user()
user_id = sp.current_user()["id"]
# User details
pprint(user_id)

# LOGIN IN SPOTIFY  {END}


# SEARCHING IN SPOTIFY  {START}

song_url = []
year = date.split("-")[0]
for song in song_names:
    song_details = sp.search(
        q=f"track:{song} year:{year}",
        limit=10,
        type="track",
        market="GB")
    # print("SD",song_details)

    try:
        track_uri = song_details["tracks"]["items"][0]["uri"]
        song_url.append(track_uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        pass
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")



print("Song list",song_url)

# SEARCHING IN SPOTIFY  {END}



# CREATING PLAYLIST AND STORING IT IN PLAYLIST {START}

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print("PlayList",playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_url)

# CREATING PLAYLIST AND STORING IT IN PLAYLIST {END}