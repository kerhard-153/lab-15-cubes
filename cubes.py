import matplotlib.pyplot as plt

x_values_1 = [1, 2, 3, 4, 5]
y_values_1 = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()

ax.plot(x_values_1, y_values_1, linewidth=2)

ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()