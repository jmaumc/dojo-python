import pandas as pd
import requests

pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"

nba = pd.read_csv(download_url)

#print(f"Shape: {nba.shape}")
#print(f"N. rows: {len(nba)}")
print(nba.head(10))
#print(nba.tail(10))

#print(nba.info)
print(nba.loc[nba['fran_id'] == 'Lakers', 'team_id'].value_counts())
print(nba.loc[nba['team_id'] == 'MNL', 'date_game'].max())
nba['date_played'] = pd.to_datetime(nba['date_game'])
print(nba.info())
total_bos_points = nba.loc[nba['team_id'] == 'BOS', 'pts'].sum()
years_bos_played = len(nba.loc[nba['team_id'] == 'BOS', 'date_played']\
    .apply(lambda v: v.year).unique())
avg_bos_points_per_year = total_bos_points / years_bos_played
print(avg_bos_points_per_year)

