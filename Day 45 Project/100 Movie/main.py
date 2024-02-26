import requests 
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
website_html = response.text

soups = BeautifulSoup(website_html, "html.parser")

# print(soups.prettify())

all_movies = soups.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in all_movies]
# for n in range(len(movies_titles) - 1, -1, -1):
#     print(movies_titles[n])
movies = movies_titles[::-1]

with open ("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

