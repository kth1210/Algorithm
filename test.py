import math
import numpy as np
import matplotlib.pyplot as plt

def func_cos(x, n):
  cos_approx = 0
  for i in range(n):
    coef = (-1)**i
    num = x**(2*i)
    denom = math.factorial(2*i)
    cos_approx += (coef) * ((num) / (denom))

  return cos_approx
  
angles = np.arange(-2*np.pi, 2*np.pi, 0.1)
p_cos = np.cos(angles)

fig, ax = plt.subplots()
ax.plot(angles, p_cos)

for i in range(1, 6):
  t_cos = [func_cos(angle, i) for angle in angles]
  ax.plot(angles, t_cos)
  print("here")


ax.set_ylim([-7,4])

plt.show()