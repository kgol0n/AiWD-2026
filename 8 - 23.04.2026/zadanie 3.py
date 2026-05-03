import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.arange(0, 31, 0.1)
sinus = np.sin(x)
cosinus = np.cos(x)

plt.plot(x, sinus, label="sin(x)", color="royalblue")
plt.plot(x, cosinus, label="cos(x)", color="orange")
plt.title("Wykres sin(x) i cos(x)")
plt.xlabel("x")
plt.ylabel("funkcje trygonometryczne")
plt.legend(loc=6)
plt.show()