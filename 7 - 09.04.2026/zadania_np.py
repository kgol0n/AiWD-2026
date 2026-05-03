import numpy as np
arr = np.array([[0,1,2,3], [10,11,12,13], [40,41,42,43]])

# 1 
srednia = np.mean(arr, axis=1)
print(srednia[0])
print(srednia[1])
print(srednia[2])

# 2
arr[:2, 1] = -3
print(arr)

# 3
print((arr > 25).sum())

# 4
arr[arr % 2 == 0] = 0
print(arr)