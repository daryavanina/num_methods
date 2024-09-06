def half_division (func, x0, x1, eps=1e-3):
    if func(x0)*func(x1)<0:
        if abs(x0-x1) < eps:
            return x1
        x2 = (x0+x1)/2
        if func(x0)*func(x2)<0:
            return half_division(func,x0,x2)
        else:
             return half_division(func,x1,x2)

def func (x):
    return x**3+8*x**2+5*x-14

answer_by_method = half_division(func, -3, 0)

print(answer_by_method)
print(func(answer_by_method))
print(func(-2))