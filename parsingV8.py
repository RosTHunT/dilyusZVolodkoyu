import requests
from bs4 import BeautifulSoup 


URL = 'https://kino-teatr.ua/uk/main/films_rating/order_by/title.asc.phtml?show=on'

def get_html(url):
	r = requests.get(url) 
	return r 

#html = get_html(URL)
#print(html)

def get_information(html):
	soup = BeautifulSoup(html.text,'lxml')

	informations = []
	info = soup.find_all('section', class_='uk-margin-small-top')
	
#	for info in informations:
		
	informations.append({
	'names':info.find('h1', class_="uk-h2 uk-text-uppercase").get_text(strip=True),
	'actors':info.find('div', class_="uk-width-1-2 uk-width-auto@s uk-flex-last@s uk-text-right@s tm-lh").get_text(strip=True),
	'rait':info.find('div', class_="uk-width-1-1 uk-width-auto@s uk-text-large uk-text-warning uk-margin-remove uk-text-center").get_text(strip=True),
	'golos':info.find('span', class_="uk-text-warning").get_text(strip=True),
	'opys':info.find('div', class_="uk-width-1-1 uk-margin-small-top tm-lh tm-fa").get_text(strip=True),
	'link_product':info.find('a', class_="uk-link-reset").get('href')
			})

	rprint(informations)

html = get_html(URL)
result = get_information(html)
#print(result)