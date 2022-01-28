import requests
import webbrowser
from bs4 import BeautifulSoup 


url = 'https://kino-teatr.ua/uk/film/venom-letre-be-carnage-51152.phtml'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#<h1 class="uk-h2 uk-text-uppercase">Фільм <span itemprop="name">Веном 2: Карнаж</span></h1>  назва фільму
names = soup.find('h1', class_="uk-h2 uk-text-uppercase").text.strip()

print(names)

# <div class="uk-width-1-2 uk-width-auto@s uk-flex-last@s uk-text-right@s tm-lh">

actors = soup.find('div', class_="uk-width-1-2 uk-width-auto@s uk-flex-last@s uk-text-right@s tm-lh").text.strip()

print(actors)

#<div class="uk-width-1-1 uk-width-auto@s uk-text-large uk-text-warning uk-margin-remove uk-text-center">8.5 / <span itemprop="bestRating">10</span></div>
rait = soup.find('div', class_="uk-width-1-1 uk-width-auto@s uk-text-large uk-text-warning uk-margin-remove uk-text-center").text.strip()

print(rait)

#<div> Голосів: <span class="uk-text-warning" itemprop="ratingCount">1757</span> </div>
golos = soup.find('span', class_="uk-text-warning").text.strip()

print(golos)


#<div class="uk-width-1-1 uk-margin-small-top tm-lh tm-fa" itemprop="description">
#				<p style="text-align: justify;">&nbsp;Друге пришестя Венома з Томом Гарді у головній ролі! Фантастичний блокбастер виходить на новий рівень екшну і візуальних ефектів. Над світом нависла загроза. Тандем Едді Брока та інопланетного симбіота Венома кидає свою силу проти нового ворога - нестримного монстра-вбивці Карнажа.</p>			</div>



opys = soup.find('div', class_="uk-width-1-1 uk-margin-small-top tm-lh tm-fa").text.strip()

print(opys)

print('https://kino-teatr.ua/public/main/films/trailer_20362.mp4')
webbrowser.open('https://kino-teatr.ua/public/main/films/trailer_20362.mp4')






#<h1 class="uk-h2 uk-text-uppercase">Фільм <span itemprop="name">Веном 2: Карнаж</span></h1>  назва фільму
### <div class="uk-width-1-2 uk-width-auto@s uk-flex-last@s uk-text-right@s tm-lh">
#				В ролях: <br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Том Гарді" href="https://kino-teatr.ua/uk/person/hardy-tom-3283.phtml" itemprop="name">Том Гарді</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Вуді Гаррельсон" href="https://kino-teatr.ua/uk/person/harrelson-woody-859.phtml" itemprop="name">Вуді Гаррельсон</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Мішель Вільямс" href="https://kino-teatr.ua/uk/person/williams-michelle-424.phtml" itemprop="name">Мішель Вільямс</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Наомі Гарріс" href="https://kino-teatr.ua/uk/person/harris-naomie-3530.phtml" itemprop="name">Наомі Гарріс</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Рейд Скотт" href="https://kino-teatr.ua/uk/person/scott-reid-13819.phtml" itemprop="name">Рейд Скотт</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Стівен Ґрем" href="https://kino-teatr.ua/uk/person/graham-stephen-10961.phtml" itemprop="name">Стівен Ґрем</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Пеґґі Лу" href="https://kino-teatr.ua/uk/person/lu-peggy-21775.phtml" itemprop="name">Пеґґі Лу</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Мішель Ґрінідж" href="https://kino-teatr.ua/uk/person/greenidge-michelle-21774.phtml" itemprop="name">Мішель Ґрінідж</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Лоуренс Спеллман" href="https://kino-teatr.ua/uk/person/spellman-laurence-19261.phtml" itemprop="name">Лоуренс Спеллман</a>
#					</span><br>
#									<span itemprop="actor" itemscope="" itemtype="https://schema.org/Person">
#						<a target="_blank" title="Шон Делані" href="https://kino-teatr.ua/uk/person/delaney-sean-21773.phtml" itemprop="name">Шон Делані</a>
#					</span><br>
#								<a href="https://kino-teatr.ua/uk/film-persons/venom-letre-be-carnage-51152.phtml">Всі учасники...</a>
#			</div>




#			в ролях


#<div class="uk-width-1-1 uk-width-auto@s uk-text-large uk-text-warning uk-margin-remove uk-text-center">8.5 / <span itemprop="bestRating">10</span></div>
# рейтинг



#<div>
#		Голосів: <span class="uk-text-warning" itemprop="ratingCount">1757</span>
#	</div>
#голоси


#<p style="text-align: justify;">&nbsp;Друге пришестя Венома з Томом Гарді у головній ролі! Фантастичний блокбастер виходить на новий рівень екшну і візуальних ефектів. Над світом нависла загроза. Тандем Едді Брока та інопланетного симбіота Венома кидає свою силу проти нового ворога - нестримного монстра-вбивці Карнажа.</p>
#опис


#<video width="660" height="356" controls="controls" poster="https://kino-teatr.ua/public/main/films/2021-10/trailer_20362.jpg" style="float:left">
#					<source src="https://kino-teatr.ua/public/main/films/trailer_20362.mp4" type="video/mp4">
#					<p class="uk-text-center">
#						Для перегляду цього відео необхідно ввімкнути JavaScript, та оновити браузер з підтримкою HTML5					</p>
#				</video>
