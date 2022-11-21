import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

def func(t):
    ff = 53.39 * (1 - np.exp(-0.18355 * t))
    return ff

xx = np.linspace(0, 14, 500)
yy = [func(b) for b in xx]

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1, 1, 1)

plt.plot(xx, yy)
plt.show()

# print("t,s : {}    v,m/s : {}" .format(0, func(0)))
# print("t,s : {}    v,m/s : {}" .format(2, func(2)))
# print("t,s : {}    v,m/s : {}" .format(4, func(4)))
# print("t,s : {}    v,m/s : {}" .format(6, func(6)))
# print("t,s : {}    v,m/s : {}" .format(8, func(8)))
# print("t,s : {}    v,m/s : {}" .format(10, func(10)))
# print("t,s : {}    v,m/s : {}" .format(12, func(12)))
# print("t,s : {}    v,m/s : {}" .format(14, func(14)))
