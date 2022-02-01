import requests
from bs4 import BeautifulSoup 


URL = 'https://kino-teatr.ua/uk/film/venom-letre-be-carnage-51152.phtml'
#response = requests.get(URL)
#soup = BeautifulSoup(response.text, 'lxml')

def get_html(url):
	r = requests.get(url) 
	return r 

#html = get_html(URL)
#print(html)

#uk-grid uk-grid-small uk-margin-remove uk-padding-small uk-grid-stack
def get_information(html):
	soup = BeautifulSoup(html.text,'lxml')

	informations = []
	
#	for info in informations:
		
	informations.append({
	'names':soup.find('h1', class_="uk-h2 uk-text-uppercase").get_text(strip=True),
	'actors':soup.find('div', class_="uk-width-1-2 uk-width-auto@s uk-flex-last@s uk-text-right@s tm-lh").get_text(strip=True),
	'rait':soup.find('div', class_="uk-width-1-1 uk-width-auto@s uk-text-large uk-text-warning uk-margin-remove uk-text-center").get_text(strip=True),
	'golos':soup.find('span', class_="uk-text-warning").get_text(strip=True),
	'opys':soup.find('div', class_="uk-width-1-1 uk-margin-small-top tm-lh tm-fa").get_text(strip=True)
			})
#	informations.append([names, actors, rait, golos, opys])
#	for info in informations.items:
	
	return informations
	for info in informations.items:
		print(info)

#	print(informations)

#html = get_html(URL)
#get_information(html)
html = get_html(URL)
result = get_information(html)
print(result)