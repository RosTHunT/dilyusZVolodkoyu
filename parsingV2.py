import requests
from bs4 import BeautifulSoup

HOST = 'https://kino-teatr.ua/'
URL = 'https://kino-teatr.ua/uk/main/films_rating/order_by/title.asc.phtml?show=on'
HEADERS = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
	}

#звернутись до сайту
def get_html(url, params=''):
	r = requests.get(url, headers = HEADERS, params=params) 
	return r 

#получає контент
def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_="uk-grid uk-grid-small uk-grid-match uk-child-width-1-1 uk-flex")
	films = []
	
	#логіка для складання інфи в фільми циклом
	for item in items:
		films.append(
			{
			'information':item.find('div', class_="uk-width-expand@s").get_text(strip=True),
			'link_information':item.find('div', class_="uk-width-expand@s").find('a').get('href'),
			'Name':item.find('h2', class_="uk-h4").get_text(strip=True),





#			'image':item.find('div', class_="uk-width-3-4 uk-width-1-1@s uk-box-shadow-small").find('img').get('src'),
#			'image':item.find('div', class_="uk-width-3-4 uk-width-1-1@s uk-box-shadow-small").find('img').get('src')
#			'image':item.find('div', class_="uk-width-3-4 uk-width-1-1@s uk-box-shadow-small").find('img').get('src')	

#			'golos':item.find('div', class_="uk-width-expand@s").find('span').get(id='span_rating_val_53637'),
#			'actors':item.find('div', class_="uk-width-1-2 uk-width-auto@s uk-flex-last@s uk-text-right@s tm-lh").get_text(),
#			'rait':item.find('div', class_="uk-text-center uk-text-warning uk-width-1-3 uk-first-column").get_text(strip=True),
#			'golos':item.find('a', class_="uk-margin-small-bottom").get_text(),
#			'opys':item.find('a', class_="uk-margin-small-bottom").get_text(),
#			'link_product':HOST + item.find('a', class_="uk-margin-small-bottom").get_text(),
			}
			)
		return films	 
#html = get_html(URL)
#print(get_content(html.text))

def parser():
	PAGENATION = input('вкажіть кількість сторінок')
	PAGENATION = int(PAGENATION.strip())
	html = get_html(URL)
	films = []
	for page in range(1, PAGENATION):
		print(f'парсимо сторінку: {page}')
		html = get_html(URL, params={'page': page})
		films.extend(get_content(html.text))
	print(films)
parser()			
