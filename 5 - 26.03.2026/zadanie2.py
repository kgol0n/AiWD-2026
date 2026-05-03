import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('./datasets/imiona.xlsx')
seria2 = df.groupby('Plec')['Liczba'].sum()
colors = {'K':'purple', 'M':'orange'}
seria2.plot.bar(title='Całkowita liczba urodzonych chłopców i dziewczynek',
            xlabel='Płeć',
            ylabel='Liczba urodzeń',
            color=[colors[p] for p in seria2.index],
            figsize=(6,6))
plt.show()