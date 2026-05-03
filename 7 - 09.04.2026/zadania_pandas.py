import pandas as pd
import numpy as np
# pycharm i dokumentacja
df = pd.read_csv('powtorzenie.csv', sep=';')


# 1
df = df.dropna(axis=1)
# print(df)

# 2
srednia = df[df['wiek'] > 20]['wynik'].mean()
# print(srednia)

# 3 - tu nie wiem jak zrobić bez for
df["test_zaliczony"] = True
# print(df)

# 4 - zrobic w jednej linii kodu
srednia_nzal = df[df['wynik'] < 50]['wynik'].mean()
srednia_zal = df[df['wynik'] > 50]['wynik'].mean()
# print(f'Srednia dla nzal: {round(srednia_nzal, 2)}')
# print(f'Srednia dla zal: {round(srednia_zal, 2)}')

# 5
imiona = df.sort_values('wiek')['imie'][(df['wynik'] >= 50)].head(5)
print(imiona.to_string(index=False))