def distinct_number(number):
    numbers = []
    for i in str(number):
        if i not in numbers:
            numbers.append(i)
        else:
            return f"Not all numbers are distinct. {number}"
    return f"Yes All numbers are distinct. {number}"


print(distinct_number(123))

