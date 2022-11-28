import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 82, 90, 95, 100, 103, 110, 115, 120, 125])
y = np.array([240, 250, 264, 270, 280, 290, 294, 310, 320, 330])

plt.title("Health Chart")

plt.plot(x, y)

plt.grid(color = 'yellow', linestyle = '--', linewidth = 1.5)

plt.show()
