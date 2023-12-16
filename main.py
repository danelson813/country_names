# utils/util.py
import pandas as pd
from utils.util import get_soup, parse


url = 'https://www.scrapethissite.com/pages/simple/'
soup = get_soup(url)

jobs = soup.find_all('div', class_='col-md-4 country')

results = []
for job in jobs:
    country_title = job.find('h3', class_='country-name').text.strip()

    info_ = job.find('div', class_='country-info').text
    cap_ = info_.split("\n")   
    info = parse(cap_)

    capital = info[0]
    population = info[1]
    area = info[2]

    result = {
        'country': country_title,
        'capital': capital,
        'population': population,
        'area_km2': area
    }
    results.append(result)

df = pd.DataFrame(results)
df.to_csv('data/results.csv', index=False)
