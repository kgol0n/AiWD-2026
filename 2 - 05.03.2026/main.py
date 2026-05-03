#%%
import numpy as np

tablica = np.arange(2, 42, 2)
print(tablica)

#%%
import numpy as np

liczby = [0.1, 16.2, 3.6]
print(liczby)
print(type(liczby[0]))
b = np.array(liczby, 'int64')
print(b)
print(type(b))
print(b.dtype)

#%%
import numpy as np

def calkowite(n:int):
    tablica = np.empty((n, n), 'int64')
    liczba = 1
    for i in range(0, 5):
        for j in range(0, 5):
            tablica[i, j] = liczba
            liczba += 1
    print(tablica)
calkowite(5)

#%%
import numpy as np

def potegi(a, n):
    tablica = np.logspace(1, 5, base=a, num=n, dtype=int)
    print(tablica)

potegi(2, 5)

#%%
import numpy as np

def wektory(n:int):
    wektor = [i for i in range(1, n+1)]
    wektor.reverse()

    mat_diag = np.diag(wektor)
    print(mat_diag)

wektory(3)


def generuj_macierz(n):
    nowy_wektor = np.arange(n, 0, step=-1)
    nowa_macierz = np.diag(nowy_wektor)
    return nowa_macierz
print(generuj_macierz(3))


