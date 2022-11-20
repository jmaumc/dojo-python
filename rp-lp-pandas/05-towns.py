# %%
import pandas as pd


def read():
    towns = []
    state = ''
    with open('datasets/university_towns.txt', mode='r') as file:
        for line in file:
            if '[edit]' in line:
                state = line.strip()
            else:
                towns.append([state, line])
    return pd.DataFrame(towns, columns=['state', 'towns']).assign(
        state=lambda df: df.loc[:, 'state'].str.removesuffix('[edit]'),
        towns=lambda df: df.loc[:, 'towns'].str.extract(r'(.*) \(.*')
    )

towns = read()
# %%
