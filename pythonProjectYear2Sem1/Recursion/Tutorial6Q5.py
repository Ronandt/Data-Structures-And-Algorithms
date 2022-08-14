#a
def exp(x,n):
    return x**n
print(exp(5,3))

#b
def exp_recursive(x,n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (x) * (exp_recursive(x,n-1))
print(exp_recursive(2,8))
