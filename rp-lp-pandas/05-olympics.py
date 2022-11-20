# %%
import pandas as pd


def read():
    return pd.read_csv('datasets/olympics.csv', header=1).rename(
        columns={
            'Unnamed: 0': 'country',
            '? Summer': 'summer_olympics',
            '01 !': 'summer_golds',
            '02 !': 'summer_silvers',
            '03 !': 'summer_bronzes',
            'Total': 'summer_total',
            '? Winter': 'winter_olympics',
            '01 !.1': 'winter_golds',
            '02 !.1': 'winter_silvers',
            '03 !.1': 'winter_bronzes',
            'Total.1': 'winter_total',
            '? Games': 'total_games',
            '01 !.2': 'total_golds',
            '02 !.2': 'total_silvers',
            '03 !.2': 'total_bronzes',
            'Combined total': 'combined_total'
        }
    )

olympics = read()

# %%
