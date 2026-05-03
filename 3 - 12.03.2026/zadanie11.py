import numpy as np

vector = np.array([np.random.randint(1,100) for i in range(12)]).reshape((3,4))
print(vector)
vector_2 = vector.reshape((4,3)).ravel()
vector_3 = vector.reshape((2,6)).ravel()

print(vector_2)
print(vector_3)