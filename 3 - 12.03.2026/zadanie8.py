import numpy as np

macierz = np.array([np.random.randint(1,100) for i in range(9)]).reshape((3,3))
for i in range(3):
    print(f'Wiersz {i+1}: {macierz[i]}')
