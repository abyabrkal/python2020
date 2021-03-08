# 
# PROJECT: SPOTIFY PLAYLIST from BILLBOARD TOP 100 of any past date
# 


from bs4 import BeautifulSoup
import requests

URL = 'https://www.billboard.com/charts/hot-100/'

time = input("Which year you want to travel to (Enter YYYY-MM-DD)? ").strip()

response = requests.get(f'{URL}{time}')
bilhot100 = response.text

soup = BeautifulSoup(bilhot100, 'html.parser')
all_songs = soup.find_all(name='span', class_='chart-element__information__song')

song_titles = [song.getText() for song in all_songs]
print(song_titles)
