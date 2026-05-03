# zadanie 1a

import numpy as np

# zadanie 1a
tablica = np.zeros((20,5), dtype=int)

for i in range(0,20):
    for j in range(0, 5):
        tablica[i][j] = np.random.randint(0,101)
# print(tablica)

# zadanie 1b
import pandas as pd
df = {"Matematyka" : tablica[0], "Chemia": tablica[1], "Fizyka": tablica[2], "Biologia":tablica[3],
      "Informatyka":tablica[4]}
df = pd.DataFrame(df)
# print(df)

# zadanie 1c (tu trzeba zrobic funkcjami)
df["Średnia"] = (df["Matematyka"] + df["Chemia"] + df["Fizyka"] + df["Biologia"] + df["Informatyka"]) / 5
# df["Średnia_2"] = int(df.loc[0:4]).mean()
# print(df)

# zadanie 1d
df["Ocena"] = 0

for i in range(0, 5):
    print(df.loc[i]["Średnia"])
    if df.loc[i]["Średnia"] <= 40:
        df.loc[i, "Ocena"] = 2
    elif df.loc[i]["Średnia"] <= 60:
        df.loc[i, "Ocena"] = 3
    elif df.loc[i]["Średnia"] <= 80:
        df.loc[i, "Ocena"] = 4
    else:
        df.loc[i, "Ocena"] = 5

# print(df)



 
