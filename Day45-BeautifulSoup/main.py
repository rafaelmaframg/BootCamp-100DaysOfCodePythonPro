from bs4 import BeautifulSoup
import requests


r = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(r.text, "html.parser")

teste = soup.find_all(name="h3", class_="title" )
for film in teste:
    print(film.getText())
