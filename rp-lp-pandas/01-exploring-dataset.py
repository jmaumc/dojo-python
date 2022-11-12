import pandas as pd
import requests

pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"

nba = pd.read_csv(download_url)

print(f"Shape: {nba.shape}")
print(f"N. rows: {len(nba)}")
#print(nba.head(10))
#print(nba.tail(10))

print(nba.info)
