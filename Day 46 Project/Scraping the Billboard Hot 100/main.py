import requests
from bs4 import BeautifulSoup


desired_date = input("What date would you like to go back to? Type date in this format: YYYY-MM-DD ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{desired_date}")
music_data = response.text

soup = BeautifulSoup(music_data,"html.parser")
songs = soup.select("li ul li h3")
songs_titles = [song.getText().strip() for song in songs]
print(songs_titles)
