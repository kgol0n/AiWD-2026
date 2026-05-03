import numpy as np


# zadanie 7

# def tworzenie_macierzy(n):
#     # przyklad rozwiazania 1
#     macierz = np.diag([2]*n)
#     print(macierz)
#
#
#
#
#     # przyklad rozwiazania 2
#     nowa_lista = []
#     for a in range(n):
#         nowa_lista.append(2)
#     macierz = np.diag(nowa_lista)
#     print(macierz)
#     return macierz
#
# print(tworzenie_macierzy(3))


def tworzenie_macierzy(n):
    macierz = np.diag([2]*n)
    for i in range(1, n+1):
        np.fill_diagonal(macierz[i:], 2*i+2)
        np.fill_diagonal(macierz[:, i:], 2 * i + 2)
    return macierz
print(tworzenie_macierzy(4))