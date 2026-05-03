import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dane/iris.data', sep=',', header=None)
# 0 - sepal length, 1 - sepal width
df = df.drop([2,3], axis=1)
df = df.rename(columns={0:"sepal length", 1:"sepal width", 4:"class"})

x = df['sepal length']
y = df['sepal width']

plt.scatter(x, y, c= np.random.randint(0, 150, 150))
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()