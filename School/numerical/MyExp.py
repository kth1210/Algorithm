import math

def IterMeth(val, es, maxit):
  iter = 1
  sol = val
  ea = 100

  while iter < maxit and ea > es:
    solold = sol
    sol += math.pow(val, iter) / math.factorial(iter)

    iter += 1

    if sol != 0:
      ea = abs((sol - solold) / sol) * 100

  return sol, ea, iter


v = float(input('E의 몇승까지 구할지 실수 입력 : '))
e = float(input('함수의 허용 오차범위 입력 : '))
m = float(input('최대 루프값 입력 : '))

[val, ea, iter] = IterMeth(v, e, m)
print("val = ")
print(val)
print("ea = ")
print(ea)
print("iter = ")
print(iter)