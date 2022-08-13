def num_vowels(text):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in text:
        if i.lower() in vowels:
            count+=1
    return count

print(num_vowels('Apple'))

# def num_voewls(text):
#     total = 0
#     for ch in text.lower():
#         if ch in 'aeiou':
#             total+=1
#     return total