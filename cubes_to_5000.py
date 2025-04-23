import matplotlib.pyplot as plt

x_values_2 = range(1, 5001)
y_values_2 = [x**3 for x in x_values_2]

fig, ax = plt.subplots()

ax.plot(x_values_2, y_values_2, linewidth=2)

ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()