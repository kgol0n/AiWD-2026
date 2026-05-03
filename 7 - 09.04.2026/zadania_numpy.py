import numpy as np

arr = np.array([[0,1,2,3],[10,11,12,13],[40,41,42,43]])
print(arr)

# 1
for wiersz in arr:
    print(np.mean(wiersz))

# poprawne: srednie = arr.mean(axis=1)

# 2
arr[0][1] = -3
arr[1][1] = -3
# print(arr)

# 3
counter = 0
for i in range(0, 3):
    for j in range(0, 4):
        if arr[i][j] > 25:
            counter += 1
print(f'Elementy > 25: {counter}')
liczba = (arr > 25).sum()
print(liczba)


# 4
arr[arr % 2 == 0] = 0


# 5
arr = np.zeros((7,7), dtype='int')
np.fill_diagonal(arr, 3)
print(arr)
