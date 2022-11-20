# Secant
import numpy as np

delta = 0.1

def func_f(x):
  ff= np.exp(-x) - x
  return ff
  
# 함수의 정의에 대해 생각해보자!!!
def func_g(x):
  ff= x - (x+delta)*func_f(x) / (func_f(x + (x+delta)) - func_f(x))
  return ff

x0 = 1
xr = x0
es = 0.0000005
imax = 1000
iter = 0
while True:
  xrold = xr
  xr = func_g(xrold)
  iter = iter + 1
  if xr != 0 :
    ea= abs((xr - xrold) / xr) * 100
  print("iter[{}], xr[{}], ea[{}], es[{}]" .format(iter, xr, ea, es))
  if ea < es or iter >= imax :
    break;
    
Secant = xr
print(">>> secant", Secant)