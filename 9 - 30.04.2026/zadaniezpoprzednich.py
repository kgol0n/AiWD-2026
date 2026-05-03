import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# zadanie 6

#1 - wczytanie danych
df = pd.read_excel('imiona.xlsx')

#2 - utworzenie płótna
plt.figure(figsize=(16,6))

#3 - wykres nr 1
plt.subplot(1,3,1)
df_1 = df.groupby('Plec')['Liczba'].sum() #to jest seria danych
plt.bar(df_1.index, df_1.values, color=['red', 'green'])
plt.xlabel('Płeć')
plt.ylabel('Liczba narodzin')

#wykres nr 2
plt.subplot(1,3,2)
df_2 = df.groupby(by=['Plec', 'Rok'])['Liczba'].sum()
df_2_k = df_2.K
df_2_m = df_2.M
plt.plot(df_2_k.index, df_2_k, color='red', label='K')
plt.plot(df_2_m.index, df_2_m, color='green', label='M')
plt.legend()
#skala na osi x
plt.xticks(df_2_k.index,rotation=45)

#wykres nr 3
plt.subplot(1,3,3)
df_3 = df.groupby('Rok')['Liczba'].sum()
plt.bar(df_3.index, df_3)
plt.xticks(df_3.index, rotation=45)
plt.show()
