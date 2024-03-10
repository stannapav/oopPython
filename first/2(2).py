import matplotlib.pyplot as plt
import numpy as np

year = ['2023','2022','2021','2020', '2019']
uni = ['ЦДУ','КПІ']
pos = np.arange(len(year))
studentsInCUPU = [41, 44, 12, 10, 17]
studentsInKPI = [76,42,38,35,29]
barWidth = 0.2

plt.bar(pos, studentsInCUPU, barWidth, color = 'blue', edgecolor = 'black')
plt.bar(pos + barWidth, studentsInKPI, barWidth, color = 'pink', edgecolor = 'black')

plt.xticks(pos, year)
plt.xlabel('Рік', fontsize=16)
plt.ylabel('Вступників', fontsize=16)
plt.legend(uni, loc='upper right')
plt.show()
