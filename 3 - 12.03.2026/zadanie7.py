import numpy as np

macierz = np.array([[1,2,3], [4,5,6]])
a = np.ones((2,3))
b = np.ones((2,3))
for i in range(2):
    for j in range(2):
        a[i][j] = np.sin(macierz[i][j])
        b[i][j] = np.cos(macierz[i][j])

print(a+b)