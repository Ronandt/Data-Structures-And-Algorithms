def minmax(data): #Q!
    small = big = data[0]
    for x in data:
        if x > big:
            big = x
        elif x < small:
            small = x
    return(big, small)


def sum_of_squares(data: int): #Q2
    return sum([x**2 for x in range(data + 1)])

def sum_of_squares_odd(data: int):#Q3
    #sum([x**2 for x in range(max(1, data+1), 2)]) #second way
    return sum([x**2 for x in range(max(1, data+1)) if x//2 == x/2])


def range_constructor() -> list: #Q4
    return range(50, 81, 10), range(8, -9, -1)

def num_vowels(text: str) -> int: #Q5
    #len(filter(lambda x:x in "aeiou"), text) #one way
    return len([x for x in text if x in "aeiou"])

def err():
    lists = []
    try:
        while True:
            line = input('Enter a line (ctrl-D to stop):')
            lists.append(line)
    except EOFError:
        print('^D')
        print('\n'.join(reversed(lists)))


def distinct(data): #Q7
     for k in range(1, len(data)):
        for j in range(k):
             if data[j] == data[k]:
                 return False
     return True




