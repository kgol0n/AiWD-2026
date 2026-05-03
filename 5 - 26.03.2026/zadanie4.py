import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/zamowienia.csv', sep=';')

#dane = df.groupby('Sprzedawca').size() - #to tez dziala
dane = df['Sprzedawca'].value_counts()
colors = np.random.rand(len(dane), 3)
dane.plot.barh(
    ylabel='Sprzedawca',
    xlabel='Liczba zamowien',
    title='Liczba zamowien dla poszczegolnych sprzedawcow',
    color=colors,
    rot=45
)
plt.show()
