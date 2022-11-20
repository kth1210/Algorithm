# Newton Raphson
import numpy as np

def func_f(x):
  ff= x**10 - 1
  return ff

def func_g(x):
  ff= x - ((x**10 - 1) / (10*(x**9)))
  return ff

x0 = 0.5
xr = x0
es = 0.0001
imax = 10000
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

NewtonRaphson = xr

print(">>> NewtonRaphson", NewtonRaphson)