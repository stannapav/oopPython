import matplotlib.pyplot as plt
import numpy as np

def vxCalc(v0, angleRad):
    return v0 * np.cos(angleRad)

def vyCalc(v0, angleRad):
    return v0 * np.sin(angleRad)

def xCalc(vx, t):
    return vx * t

def yCalc(vy, t):
    return vy * t - 0.5 * g * t ** 2

R = 0.6
angle = [20, 60, 75]
v0 = 80
g = 9.8
t = np.arange(0, 16, 0.0001)

for i in angle:
    vx = vxCalc(v0, np.deg2rad(i))
    vy = vyCalc(v0, np.deg2rad(i))

    x, y = [], []
    for j in t:
        x.append(xCalc(vx, j))
        y.append(yCalc(vy, j))

        if y[-1] < 0: break

    plt.plot(x, y, label = f'angle = {i}')

plt.grid()
plt.legend()
plt.show()