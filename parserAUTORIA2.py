import requests
from bs4 import BeautifulSoup 
import csv


HOST = 'https://auto.ria.com/uk'
URL = 'https://auto.ria.com/uk/newauto/marka-renault/'
HEADERS = {
	'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
	}
FILE = 'cars.csv'





def get_html(url, params=''):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def get_pages_count(html):
	soup = BeautifulSoup(html, 'html.parser')
	pagination = soup.find_all('span', class_="page-item mhide")
	if pagination:
		return int(pagination[-1].get_text())
	else:
		return 1	


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='proposition_link')
    
    cars = []

    for item in items:

    	usd_price =	item.find('span', class_="green")
    	if usd_price:
    		usd_price = usd_price.get_text(strip=True)
    	else:
    		usd_price = 'зверніться за ціною'

    	uah_price =	item.find('span', class_="size16")
    	if uah_price:
    		uah_price = uah_price.get_text(strip=True)
    	else:
    		uah_price = 'зверніться за ціною'	

    	cars.append({
    		'title': item.find('div', class_='proposition_title').get_text(strip=True),
    		'link': HOST + item.get('href'),
    		'usd_price': usd_price,
			'uah_price': uah_price,
			'city': item.find('span', class_="item region").get_text(strip=True),
    		})
    return cars
	



def save_file(items, path):
	with open(path, 'w', newline='') as file:
		writer = csv.writer(file, delimiter=';')
		writer.writerow(['марка','ссилка','ціна гривні','ціна в доларах','місто'])	
		for item in items:
			writer.writerow([item['title'], item['link'], item['uah_price'], item['usd_price'], item['city']])


def parse() :
	html = get_html(URL)
	if html.status_code == 200:
		cars = []
		pages_count = get_pages_count(html.text)
		for page in range(1, pages_count + 1) :
			print(f'Парсимо сторінку {page} з {pages_count}....')
			html = get_html(URL, params={ 'page':page})
			result = get_content(html.text)
			cars.extend(result)
		save_file(cars, FILE)	


		print(f'Отримано інформацію з {len(cars)} сторінок')	
		get_content(html.text)
	else:
		print('Error')		


parse()












#html = get_html(URL)
#a = get_content(html.text)


#    cars = []
#
#    for item in items:
#       uah_price = item.find('span', class_='grey size13')
#        if uah_price:
#            uah_price = uah_price.get_text()
#        else:
#            uah_price = 'Цена в гривнах не указана'
#        href = HOST + item.find('a').get('href')
#        title = item.get_text(strip=True)
#        cars.append({
#            'title': title,
#            'link': href,
#            'usd_price': item.find('span', class_='green').get_text(),
#            'uah_price': uah_price,
#            'city': item.find('svg', class_='svg-i16_pin').find_next('strong').get_text(),
#
#        })

#    print(cars)	