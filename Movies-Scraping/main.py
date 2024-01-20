import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webstie_html = response.text

soup = BeautifulSoup(webstie_html, "html.parser")

title = soup.find_all(name= "h3", class_ = "title")
# print(title)

movies_title = [ movie.getText() for movie in title]
# print(movies_title[::-1])  #Reverse List
movies = movies_title[::-1]

# 2nd
# movies = []
# for n in range(len(movies_title) -1, 0, -1):
#     # print(movies_title[n])
#     movies.append(movies_title[n])

# Write movies in txt
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for m in movies:
        file.write(f"{m}\n")

