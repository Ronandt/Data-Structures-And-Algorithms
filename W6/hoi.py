'''def summing(x):
    print(x)
    if x == 1:
        return 1
    return x +summing(x-1)
print(summing(10))

def sumDigits(n, index):
    if len(str(n)) -1 == index:
        return int(n[index])
    return int(n[index]) + sumDigits(n, index+1)

print(sumDigits('694234234234234242423423', 0))

def palindrome(word, first_pointer, second_pointer):

    if first_pointer == second_pointer:
        return True
    elif word[first_pointer] != word[second_pointer]:
        return False
    return palindrome(word, first_pointer + 1, second_pointer - 1)
print(palindrome(word:="racecar", 0, len(word) -1 ))

def exps(num, exp):
    if exp == 1:
        return num
    return num * exps(num, exp-1)
print(exps(2, 8))


def isPowerOfTwo( n: int) -> bool:
    if n == 1:
        return True
    elif n/2 % 1 > 0:
        return False
    return isPowerOfTwo(n/2)
print(isPowerOfTwo(8))

def sumEven(n):
    if n==2:
        return 2
    elif n%2 ==0:
        return n+sumEven(n-1)
    return sumEven(n-1)
print(sumEven(8))


numlist = [ 12, 19, 3, 13, 20, 5, 8, 16, 6, 15 ]'''
o = []
for i in range(16):
    if i % 3 == 0:
        o.append(i)
        o.append(i + 1)
    elif i % 4 == 0:
        print(i)
        del o[0]
print(o)
    
def reverse_queue(n):
    b = Stack()
    while not n.isEmpty():
        a = n.dequeue()
        b.push(a)
    while not b.isEmpty():
        n.enqueue(b.pop())
        
#dequeue_front()
#dequeue_back()
#enqueue_front()
#enqueue_back()
#isEmpty()
#length()
#Deque

def recursive(limit, txt, counter):
    print(txt)
    return str(counter) + txt + str(counter) if limit == counter else recursive(limit, str(counter) + txt + str(counter) , counter + 1)
print(recursive(3, "0", 1))

def recursive_val(limit, round, counter):
    print(counter * "#")
    if counter == 1 and round == 1:
        return recursive_val(limit, round + 1,counter+ 1 )
    elif counter == limit and round == 2:
        return ""
    elif round == 1:
        return recursive_val(limit, round, counter - 1)
    elif round == 2:
        return recursive_val(limit, round, counter + 1)    
    
#print(recursive_val(c:=480, 1, c))

'''def recursive_list(limit, counter, list):
    print(limit * "#")
    if counter == 1:
        list.insert(limit, "#")
    elif'''
    
def recursive_double(limit, counter):
    print(abs(counter) * "#")
    if counter == -limit:
        return ""
    elif counter == 1:
        return recursive_double(limit, counter - 2)
    return recursive_double(limit, counter - 1)
print(recursive_double(b:=4, b))

    
def recursive_math(n):
    if n == 0:
        print("0")
        return ""
    recursive_math(n - 1)
    print("".join(str(abs(x)) for x in range(n,-n-1,-1)))


def diamond(n):
    if n == 1:
        print("*")
        return "*"
    print(n * "*")
    diamond(n -1)
    print(n * "*")

print(diamond(3))
recursive_math(3)


def pyramid(n):
    if n == 1:
        print("*")
        return ""
    pyramid(n-1)
    print(n * "*")



def triangle(n):
    if isinstance(n, int):
        n = [str(n) + "b", str(n-1) + "a"]
    if str(n[0]) == "1b":
        print("#")
        return ""
    elif "b" in str(n[0]):
        triangle([str(int(''.join([x for x in list(n[0]) if x.isdigit()])) - 1) + "b", "c"])
        print("#" * int(''.join([x for x in list(n[0]) if x.isdigit()])))
    if str(n[1]) == "1a":
        print("#")
        return ""
    elif "a" in str(n[1]):
        print("#" * int(''.join([x for x in list(n[1]) if x.isdigit()])) )
        triangle(["c", str(int(''.join([x for x in list(n[1]) if x.isdigit()])) - 1) + "a"])


print(triangle(500))

def sequentialSearch(values, target):
    n = len(values)

    for i in range(n):
        if values > target:
            return False
        elif values[i] == target:
            return True
        
    return False

def bubble_sort_optimised(seq):
    n = len(seq)
    for i in range(n -1, 0, -1):
        noswap = True
        for j in range(i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                noswap = False
        if noswap:
            break
    return seq

def pattern(n):
    if n==1:
        print("*")
        return 0

    else:

        pattern(n-1)
        print("*" * n)
        pattern(n-1)


pattern(100)

def pat(n):
    if n ==1:
        print("#")
        return ""
    print("#" * n)
    pat(n-1)
    print("#" * n)


class Queue:
    def __init__(self):
        self._qList = list()
    def is_empty(self):
        return len(self._qList) == 0
    def __len__(self):
        return len(self._qList)
    def enqueue(self, item):
        return self._qList.append(item)
    def dequeue(self):
        assert not self.is_empty()
        return self._qList.pop(0)

class CircularQueue:
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = [None] * maxSize
    def is_empty(self):
        return not self._count
    def is_full(self):
        return None not in self._qArray
    def __len__(self):
        return self._count
    def enqueue(self, item):
        assert not self.is_full()
        max_size = len(self._qArray) 
        self._back = (self._back + 1) % max_size
        self._qArray[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.is_empty()
        self._qArray[self._front] = None
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return 
'''

1.  *

    *
2.  **
    *
    
   * 
   **
   *
3  ***
   *
   **
   *


4. *
   **
   *
   ***
   *
   ****
   *
   ***
   *
   **
   *
'''