# part (a)

def rangeConstructorA(number):
    numbers = []
    if number >= 50 and number <=80:
        for i in range(50,number+1,10):
            numbers.append(i)
        return numbers
    else:
        return f"value is not within 50 and 80"

print(rangeConstructorA(80))
print(rangeConstructorA(90))

# part (b)

def rangeConstructorB(number):
    numbers = []
    if number >= -8 and number <= 8:
        for i in range(-8, number + 1, 2):
            numbers.append(i)
        return numbers
    else:
        return f"value is not within -8 and 8"

print(rangeConstructorB(8))
print(rangeConstructorB(-10))

