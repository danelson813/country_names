import pandas as pd
from utils.util import get_soup, get_url
import sqlite3

results = []
for i in range(1,13):
    url = get_url(i)
    soup = get_soup(url)

    rows = soup.select('tr.team')
    for row in rows:
        team = row.select_one('.name').get_text().strip()
        year = row.select_one('.year').get_text().strip()
        wins = row.select_one('.wins').get_text().strip()
        losses = row.select_one('.losses').get_text().strip()
        ot_losses = " "
        win_percentage = row.select_one('.pct').get_text().strip()
        gf = row.select_one('.gf').text.strip()
        ga = row.select_one('.ga').text.strip()
        diff = row.select_one('.diff').text.strip()
        result = {
            'Team_Name': team,
            'Year': year,
            'Wins': wins,
            'Losses': losses,
            'OT_lLosses': ot_losses,
            'Win_%': win_percentage,
            'Goals_For_GF': gf,
            'Goals_Against_GA': ga,
            '+ / -': diff
        }
        results.append(result)
    
df = pd.DataFrame(results)
df.to_csv('data/Hockey.csv', index=False)

conn = sqlite3.connect('data/hockey.sqlite')
df.to_sql('stats', conn, if_exists='replace', index=False)
new_df = pd.read_sql('select * from stats', conn)
print(new_df.head())