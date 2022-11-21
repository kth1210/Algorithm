import numpy as np

x = int(input("x : "))
es = float(input("es : "))
maxit = int(input("MaxIter : "))

iter = 1
sol = 1
ea = 100
fac = 1

while True:
    solold = sol
    fac = fac * iter
    sol = sol + x ** iter / fac
    iter = iter + 1

    if sol != 0:
        ea = abs((sol - solold) / sol) * 100
    
    print("iter : {}, sol = {}, ea = {}, es = {}" .format(iter, sol, ea, es))
    
    if ea <= es or iter >= maxit:
        break