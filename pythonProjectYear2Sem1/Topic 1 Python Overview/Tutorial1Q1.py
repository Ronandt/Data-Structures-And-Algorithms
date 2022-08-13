def minmax(data):
    small = big = data[0]
    for val in data:

        if val < small:
            small = val
        elif val > big:
            big = val

    return f"Lowest number is {small} and Higest number is {big}"


TestData = [10,14,15,18]
result = minmax(TestData)
print(result)