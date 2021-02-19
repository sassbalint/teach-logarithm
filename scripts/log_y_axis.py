"""
Display a demo graph with log y axis for teaching logarithm.
"""

from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


def load():
    """Load."""

    data = defaultdict(lambda: defaultdict(int))

    for year in range(2007, 2014):
        with open(f'data/{year}_noi_00.csv', encoding='utf-8') as infile:
            next(infile) # skip first line
            for line in infile:
                try:
                    _, name, freq = line.strip().split('\t')
                except ValueError:
                    (_, name), freq = line.strip().split('\t'), '0'
                name = name.strip('"')
                name = name[0] + name[1:].lower()
                data[year][name] = int(freq.replace(',', ''))

    df = pd.DataFrame.from_dict(data, orient="index") # !
    df.fillna(0, inplace=True) # !

    return df


def sample(df):
    """Sample."""

    names = [
        'Borbála', 'Sarolta', 'Iringó', 'Villő', 'Franciska',
        'Kata', 'Míra', 'Dalma', 'Veronika'
    ]

    # https://stackoverflow.com/questions/30673684
    # https://stackoverflow.com/questions/11285613
    samples = [
        df.iloc[:, list(range(0, 200, 39))], # !
        df.loc[:, names] # !
    ] 

    return samples

   
def plot(dfs):
    """Plot."""

    fig, axs = plt.subplots(2, 2, figsize=(9,10))

    yticks = [20, 50, 100, 200, 500, 1000]

    for a, df in zip(axs, dfs):

        plain, logar = a

        plain.set_title("sima")
        df.plot(ax=plain, legend=0)

        logar.set_title("logaritmikus")
        logar.set_yscale("log")
        logar.set_yticks(yticks)
        logar.get_yaxis().set_major_formatter(ScalarFormatter()) # !
        df.plot(ax=logar, legend=0)

        lh = plain.get_legend_handles_labels()
        plain.legend(*lh, bbox_to_anchor=[1, 1]) # !

    fig.suptitle('újszülöttek névgyakorisága' +
                 ' simán és logaritmikus tengelyen ábrázolva', fontsize=16)

    plt.figtext(0.99, 0.002, '(c) sassbalint@gmail.com',
        horizontalalignment='right')

    plt.tight_layout() # !

    fig.savefig('log_y_nevek.png')


def main():
    """Do the thing."""

    dataframe = load()

    samples = sample(dataframe)

    for s in samples:
        print(s.to_csv(sep='\t'))

    plot(samples)


if __name__ == '__main__':
    main()
