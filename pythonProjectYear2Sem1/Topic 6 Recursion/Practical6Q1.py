def fib(n):
    if n == 1 or n == 0:
        return n
    else :
        return fib(n-1) + fib(n-2)

num = 7
for i in range(8):
    print(fib(i))
