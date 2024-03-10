import matplotlib.pyplot as plt
import numpy as np

weight1 = [10, 13, 11, 15, 14]
length1 = [13, 15, 14, 12, 15]

weight2 = [22, 11, 20, 23, 24]
length2 = [36, 31, 35, 39, 37]

weight3 = [7, 8, 5, 9, 6]
length3 = [16, 15, 16, 20, 17]

weight = np.concatenate((weight1, weight2, weight3))
length = np.concatenate((length1, length2, length3))

plt.scatter(weight1, length1, c = 'r', label = 'American Shorthair')
plt.scatter(weight2, length2, c = 'g', label = 'Maine Coon')
plt.scatter(weight3, length3, c = 'b', label = 'Siamese')

plt.xlabel('weight', fontsize = 16)
plt.ylabel('size', fontsize = 16)
plt.title('weight(lbs) vs length(inches) of a cat', fontsize = 20)
plt.legend()
plt.show()