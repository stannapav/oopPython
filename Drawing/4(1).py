import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 5)
y = np.power(x, 4) - 2 * np.power(x, 2) - 3

ymin = min(y)
xmin = x[np.argmin(y)]

plt.plot(x, y)
plt.annotate('min', xy=(xmin, ymin), xytext=(xmin, ymin + 5), arrowprops=dict(facecolor='red', arrowstyle='wedge'))

plt.title('Графік', bbox=dict(boxstyle='square', fc='green', color='red'))

plt.show()