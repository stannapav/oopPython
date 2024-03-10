import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5)

plt.plot(x, np.sqrt(0.5 * x), 'r', label = 'y = sqrt(0.5 * x)')
plt.plot(x, np.sqrt(x), 'g', label = 'y = sqrt(x)')
plt.plot(x, np.sqrt(x) - 3, 'b', label = 'y = sqrt(x) - 3')
plt.plot(x, np.sqrt(x) + 2, 'y', label = 'y = sqrt(x) + 2')

plt.title('first')
plt.xlabel('x label')
plt.ylabel('y label')
plt.grid()
plt.legend(loc = 'best', framealpha=0.5)

plt.show()