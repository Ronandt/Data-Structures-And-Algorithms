def sumDigits(n):
    if n <= 0:
        return 0
    else:
        return (n % 10) + sumDigits(n//10)

print(sumDigits(368))