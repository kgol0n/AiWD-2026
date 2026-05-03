import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# zadanie 1 i drugie

#x i y
x = np.arange(1,21)
y = 1/x

#etykiety
plt.xlabel("x")
plt.ylabel("f(x)")
#granice
plt.ylim((0, 1))
plt.xlim((0, max(x)))

#utworzenie wykresu i legendy
plt.plot(x, y, label="f(x)=1/x", color="green", linestyle="dotted", marker=">")
plt.legend()
plt.show()