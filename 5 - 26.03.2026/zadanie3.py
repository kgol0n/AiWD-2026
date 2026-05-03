import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('./datasets/imiona.xlsx')

df1 = df[df['Rok'] > df['Rok'].max()-5]
seria3 = df1.groupby('Plec')['Liczba'].sum()

seria3.plot.pie(
    autopct='%.2f %%',
    fontsize=20,
    figsize=(6,6),
    title=f'Całkowita liczba urodzonych chłopców w latach {df['Rok'].max()-4} - {df['Rok'].max()}',
    ylabel='Liczba urodzeń'

)
plt.show()