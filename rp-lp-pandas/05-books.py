# %%
import pandas as pd


def read():
    return pd.read_csv('datasets/BL-Flickr-Images-Book.csv').rename(
        columns=lambda header: header.lower().replace(' ', '_')
    )

books = read()
# %%
