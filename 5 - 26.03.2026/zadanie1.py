import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('./datasets/imiona.xlsx')

# zadanie 1
seria1 = df.groupby('Rok')['Liczba'].sum()
seria1 = seria1/1000 # normalizacja danych, zeby bylo podanie w tysiacach

seria1.plot(title='Liczba narodzin w kazdym roku',
            xlabel='Rok',
            ylabel='Liczba urodzen [tys.]',
            figsize=(8,6), # na kolokwium ma byc widoczne
            xticks=(seria1.index),
            rot=45, # rotacja, w stopniach
            grid=True)
plt.show()