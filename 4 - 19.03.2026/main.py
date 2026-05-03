import pandas as pd
import numpy as np

df = pd.read_excel('./datasets/imiona.xlsx')

# zadanie 2.1
a = df[df['Liczba'] > 1000]
#print(a)

# zadanie 2.2
b = df[df['Imie'] == 'KACPER']
#print(b)

# zadanie 2.3
c = df.Liczba.sum()
#alternatywnie df['Liczba'].sum()
#print(c)

# zadanie 2.4
d = df.groupby('Rok')['Liczba'].sum()
#print(d)

# zadanie 2.5
e = df[(df.Rok >= 2000) & (df.Rok <= 2005)].groupby('Rok')['Liczba'].sum()
#print(e)

# zadanie 2.6
f = df.groupby('Plec')['Liczba'].sum()
#print(f)

# zadanie 2.7
g = df.groupby(['Plec', 'Imie'])['Liczba'].sum().sort_values()
g_K = g.loc['K'].idxmax() # idxmax - tam gdzie wartosc jest najwieksza
g_M = g.loc['M'].idxmax() # idxmax - tam gdzie wartosc jest najwieksza
# print(g_M)
# print(g_K)

# zadanie 2.8
min_year = df['Rok'].min()
max_year = df['Rok'].max()
print(min_year)
print(max_year)

for year in range(min_year, max_year + 1):
    x = df[(df.Rok == year)].groupby(['Plec', 'Imie'])['Liczba'].sum()
    x_K = x.loc['K'].idxmax()
    x_M = x.loc['M'].idxmax()
    print(f'Rok: {year}, M: {x_M}, K: {x_K}')
 
