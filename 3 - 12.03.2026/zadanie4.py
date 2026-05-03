import numpy as np

vector_1 = np.array([1,2,3])
vector_2 = np.array([4.4, 5.5, 6.6])

vector_3 = np.array(vector_1 * vector_2, dtype=float)
print(vector_3)