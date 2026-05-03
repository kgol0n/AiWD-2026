# Zadanie 6
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci (imiona.xlsx). Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym datasecie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel("imiona.xlsx")

suma_dziewczynek = df[df['Plec'] == 'K'].groupby('Plec')['Liczba'].sum()
suma_chlopcow = df[df['Plec'] == 'M'].groupby('Plec')['Liczba'].sum()
etykiety = ['K', 'M']
wartosci = [suma_dziewczynek, suma_chlopcow]
c = ['red', 'green']
plt.bar('K', suma_dziewczynek, color='red')
plt.bar('M', suma_chlopcow, color='green')
plt.show()