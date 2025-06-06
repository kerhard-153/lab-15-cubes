# Cubes to 5000
# Kate Erhard
# Plots numbers and their squares in the range of 1 and 5000 (inclusive)
# 4/23/25

import matplotlib.pyplot as plt

x_values_2 = range(1, 5001)
y_values_2 = [x**3 for x in x_values_2]

fig, ax = plt.subplots()
ax.scatter(x_values_2, y_values_2, c=y_values_2, cmap=plt.cm.spring, s=5)

ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()