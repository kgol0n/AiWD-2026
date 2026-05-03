import numpy as np
import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'],
    'Punktacja [%]': [85, 90, 78, np.nan, 88, 76, 92, np.nan, 80, 84],
    'Frekwencja [%]': [95, 85, np.nan, 75, 88, 92, 89, 80, np.nan, 91],
    'Zaj_dodatkowe': [True, True, False, True, False, False, False, True, False, False]
}

# zadanie 2a
df = pd.DataFrame(data)
# print(df)

# zadanie 2b
df.loc[len(df)] = ['Maria', 93.0, 75.0, True]
#print(df)

# zadanie 2c
df.loc[df['Student'] == 'Frank', 'Zaj_dodatkowe'] = True
# lokalizujemy, gdzie kolumna student ma wartosc frank, wybieramy kol zaj_dodatkowe i zmieniamy na true
#print(df)

# zadanie 2d
df = df.fillna(100)
# print(df)

# zadanie 2e
# df.to_csv('new_data.csv')

# zadanie 2f
# print(df[df['Punktacja [%]'] > 85])

# zadanie 2g
# print(round(df["Frekwencja [%]"], 2))

# zadanie 2h
# print(df.sort_values('Frekwencja [%]', ascending=True).sort_values('Punktacja [%]', ascending=False))

# zadanie 2i
mediana_chodacy = df[df['Zaj_dodatkowe'] == True]['Frekwencja [%]'].median()
mediana_niechodacy = df[df['Zaj_dodatkowe'] == False]['Frekwencja [%]'].median()
print(f'Mediana dla chodzacych na zaj. dodatkowe: {mediana_chodacy}\n'
      f'Mediana dla niechodzacych: {mediana_niechodacy}')
 
