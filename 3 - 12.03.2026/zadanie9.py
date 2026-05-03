import numpy as np

macierz = np.array([np.random.randint(1,100) for i in range(9)]).reshape((3,3))

macierz_spl = macierz.ravel()

for element in macierz_spl:
    print(element)