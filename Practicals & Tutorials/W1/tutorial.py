def minmax(data):
    small = big = data[0]
    for x in data:
        if x > big:
            big = x
        elif x < small:
            small = x
    return(big, small)


def sum_of_squares(data: int): 
    return sum([x**2 for x in range(data + 1)])

def sum_of_squares_odd(data: int):
    #sum([x**2 for x in range(max(1, data+1), 2)])
    #print(sum([x**2 for x in range(max(1, data+1)) if x & 1]))
    return sum([x**2 for x in range(max(1, data+1)) if x//2 == x/2])


def range_constructor():
    return range(50, 81, 10), range(8, -9, -1)

def num_vowels(text: str):
    len(filter(lambda x:x in "aeiou"), text)
    return len([x for x in text if x in "aeiou"])

def hash_map(text: str):
    hashmap = {}
    for x in text:
        if x in hashmap:
            return True
        hashmap[x] = x
    return False


print(sum_of_squares_odd(10))
