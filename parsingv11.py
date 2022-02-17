import requests
from bs4 import BeautifulSoup 

HOST = 'https://kino-teatr.ua/'
URL = 'https://kino-teatr.ua/uk/main/films_rating/order_by/title.asc.phtml?show=on'
HEADERS = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
	}



def get_html(url, params=''):
	r = requests.get(url, headers=HEADERS, params=params)
	return r
	

html = get_html(URL)	





def get_new_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='uk-grid uk-grid-small uk-grid-match uk-child-width-1-1 uk-flex')
    
    

    for item in items:
    
    	new_url = item.find('a').get('href'),
    
    
     
    

new_url = get_new_url(html.text)
new_html = get_html(new_url)
print(new_html)

