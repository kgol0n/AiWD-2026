import numpy as np
import matplotlib.pyplot as plt

# zadanie 1
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# t = np.linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(z)
# y = 2 * np.cos(z)
# ax.plot(x, y, z, label='zadanie 1')
# ax.legend()
# plt.show()


# zadanie 3
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np
#
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# # Generowanie danych:
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)    # tworzymy punkty o lokalizacji (X,Y)
# R = np.sqrt(X ** 2 + Y ** 2)
# Z = np.sin(R)               # nadajemy tym punktom wartości
# # Rysowanie powierzchni:
# surf = ax.plot_surface(X, Y, Z,
#                        cmap=cm.flag, linewidth=0, antialiased=False)
# ax.set_zlim(-1.01 , 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# # Dodanie paska kolorów.
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

# zadanie 4
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# 
# # konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
# fig = plt.figure(figsize=(8, 3))
# ax1 = fig.add_subplot(121, projection = '3d')
# ax2 = fig.add_subplot(122, projection = '3d')
# # fikcyjne dane
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, shade = True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
# ax2.set_title('Wykres nie zacieniony')
# plt.show()
