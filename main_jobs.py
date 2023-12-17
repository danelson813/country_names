import pandas as pd
from utils.util import get_soup
import sqlite3

url = "https://realpython.github.io/fake-jobs/"

soup = get_soup(url)

jobs = soup.select('div.card-content')

results = []
for job in jobs:
    result = {
        'title':job.select_one('h2').get_text(),
        'company': job.select_one('h3').get_text(),
        'location': job.select_one('.location').get_text().strip(),
        'date_posted': job.select_one('time').get_text()}

    results.append(result)

df = pd.DataFrame(results)
df.to_csv('data/jobs.csv', index=False)

conn = sqlite3.connect('data/jobs.sqlite')
df.to_sql('jobs', conn, if_exists='replace', index=False)
