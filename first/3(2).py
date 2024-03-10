import matplotlib.pyplot as plt

students = [25, 17, 1, 0, 10]
colors = ['b', 'g', 'r', 'c', 'm']
labels = ['Дошкільна освіта', 'Хореографія', 'Початкова освіта', 'Середня освіта(образ мистецтво)', 'Психологія']

plt.pie(students, colors=colors, labels = students, counterclock = False, shadow = True)
plt.title('ІV курс факультету психології та педагогіки')
plt.legend(labels, loc = 'best')
plt.show()