import math

# Muller's Method
# f(x) = x**3 - 13*x - 12
# x0 = 4.5, x1 = 5.5, x2 = 5
# roots are -3, -1, 4 -> (x+3)(x+1)(x-4)

def func_f(x):
  ff= x**3 - 13*x - 12
  return ff

xr = 5
h = 0.1
eps = 0.00000000001
maxit = 100

x2 = xr
x1 = xr + h*xr
x0 = xr - h*xr
print("---------------------------------")
print(f"x0 : {x0}, x1 : {x1}, x2 : {x2}")
print("---------------------------------")
iter = 0

while True :
  iter = iter + 1
  h0 = x1 - x0
  h1 = x2 - x1
  d0 = (func_f(x1) - func_f(x0)) / h0
  d1 = (func_f(x2) - func_f(x1)) / h1
  a =(d1 - d0) / (h1 + h0)
  b = a*h1 + d1
  c = func_f(x2)
  rad = math.sqrt(b*b - 4*a*c)
  if abs(b+rad) > abs(b-rad) :
    den = b + rad
  else :
    den = b - rad	
  dxr = -2*c / den
  xr = x2 + dxr
  print( f"Iter : {iter}, xr : {xr}, dxr : {dxr}")
  if abs(dxr) < eps*xr or iter >= maxit :
    break
  x0 = x1
  x1 = x2
  x2 = xr
print("")
print(f"xr : {xr}")