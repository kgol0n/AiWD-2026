import numpy as np

macierz = np.array([np.random.randint(1,100) for i in range(81)]).reshape((9,9))
print(macierz)
macierz = macierz.reshape((1,81))
print(macierz)