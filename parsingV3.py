import requests
from bs4 import BeautifulSoup 
import lxml 

URL = 'https://kino-teatr.ua/uk/film/venom-letre-be-carnage-51152.phtml'
#response = requests.get(URL)
#soup = BeautifulSoup(response.text, 'lxml')

def get_html(url):
	r = requests.get(url) 
	return r 

#html = get_html(URL)
#print(html)


def get_information(html):
	soup = BeautifulSoup(html.text,'html.parser')
	items = soup.find_all('div', class_="uk-width-2-3@m uk-padding-remove uk-first-column")
#	print(items)
	informations = []
	
	for item in items:
		informations.append(
			{
			'names':item.find('h1', class_="uk-h2 uk-text-uppercase").get_text(),
			'actors':item.find('div', class_="uk-width-1-2 uk-width-auto@s uk-flex-last@s uk-text-right@s tm-lh").text.strip(),
			'rait':item.find('div', class_="uk-width-1-1 uk-width-auto@s uk-text-large uk-text-warning uk-margin-remove uk-text-center").text.strip(),
			'golos':item.find('span', class_="uk-text-warning").text.strip(),
			'opys':item.find('div', class_="uk-width-1-1 uk-margin-small-top tm-lh tm-fa").text.strip()
			}
			)
		return informations


html = get_html(URL)
result = get_information(html)
print(result)

