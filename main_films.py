import pandas as pd
from utils.util import get_soup, parse


url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
soup = get_soup(url)

films = soup.find('tbody').find_all('tr')


results = []
for film in films[1:]:
    try:
        title = film.select_one('td:nth-of-type(1) a')['title']
    except TypeError:
        continue
    year = film.select_one('td:nth-of-type(2) > a').string
    awards = film.select_one('td:nth-of-type(3)').string
    try:
        nominations = film.select_one('td:nth-of-type(4)').string.strip()
    except AttributeError:
        continue
    result = [title, year, awards, nominations]
    results.append(result)
    

df = pd.DataFrame(results, columns=['title', 'year', 'awards', 'nominations'])
df['awards'][89] = '0(1)'

df.to_csv('data/movies.csv', index=False)
