from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# date = input("Wich year do you want to travel to? Type the date in this format YYYY-MM-DD" )
# URL = f"https://www.billboard.com/charts/hot-100/{date}"
#
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, "html.parser")
# list_musics = soup.find_all(name="div", class_="o-chart-results-list-row-container")
# for music in list_musics:
#     song = music.h3.getText().strip()
#     author = music.find(name="span", class_="a-no-trucate").get_text().strip()
#     print(song, author)


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.search("trem-bala", type="track")
print(sp.current_user())
for each in results['tracks']['items']:
    for artist in each['artists']:
        print(artist['name'])
    print(each['name'])
    print("=============")


print(sp.search("trem-bala", type="track", market="BR"))


