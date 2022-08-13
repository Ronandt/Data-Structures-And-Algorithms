def distinct_number(number):
    numbers = []
    for i in str(number):
        if i not in numbers:
            numbers.append(i)
        else:
            return f"Not all numbers are distinct. {number}"
    return f"Yes All numbers are distinct. {number}"


print(distinct_number(123))


# def distinct_numbers(numbers):
#     return len(set(numbers)) == len(numbers)


# def distinct(data):
#     for k in range(1, len(data)):
#         for j in range(k):
#             if data[j] == data[k]:
#                 return False
#     return True