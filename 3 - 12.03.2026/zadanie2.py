import numpy as np

random_num = np.random.randint(10, 51)

macierz_1 = np.zeros((3,3), dtype=int)
macierz_2 = np.zeros((4,4), dtype=int)

for i in range(3):
    for j in range(3):
        macierz_1[i][j] = np.random.randint(10,51)

for i in range(4):
    for j in range(4):
        macierz_2[i][j] = np.random.randint(10,51)

print(macierz_1)
print(macierz_2)