import matplotlib.pyplot as plt

import data

df = data.confirmed()
df[["Italy", "Spain", "US", "Canada"]].plot()
plt.show()
