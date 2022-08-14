def num_vowels(text):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in text:
        if i.lower() in vowels:
            count+=1
    return count

print(num_vowels('Apple'))

