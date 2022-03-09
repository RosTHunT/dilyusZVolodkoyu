import requests
from bs4 import BeautifulSoup

url = 'https://uakino.club/filmy/'

r = requests.get(url)
html = r.text
#print(html)
soup = BeautifulSoup(html, 'lxml')
items = soup.find_all('div', class_='movie-img')

for item in items:
	new_url = item.find('a').get('href')
	new_r = requests.get(new_url)
	new_html = new_r.text
	print(new_html)