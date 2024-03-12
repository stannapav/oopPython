import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5)
y1 = np.sqrt(0.5 * x)
y2 = np.sqrt(x)
y3 = np.sqrt(x) - 3
y4 = np.sqrt(x) + 2

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7,7))

ax[0, 0].plot(x, y1, color = 'red')
ax[0, 1].plot(x, y2, color = 'green')
ax[1, 0].plot(x, y3, color = 'blue')
ax[1, 1].plot(x, y4, color = 'yellow')

ax[0, 0].set_title('y = sqrt(0.5 * x)')
ax[0, 1].set_title('y = sqrt(x)')
ax[1, 0].set_title('y = sqrt(x) - 3')
ax[1, 1].set_title('y = sqrt(x) + 2')

plt.show()