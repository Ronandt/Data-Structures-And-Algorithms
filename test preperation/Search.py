from hashlib import new


def sortedSequentialSearch( values, target):
    n = len(values)
    for i in range(n):
        if target ==  values[i]:
            return True
        elif target < values[i]:
            break
    return False


def binary_search(values, target):
    low, high = 0, len(values) -1

    while low <= high:
        mid = (high + low)//2
        if values[mid] == target and (values[max(0, mid -1)] != target or not mid-1):
            return True
        elif values[mid] > target:
            high = mid  - 1

        else:
            low = mid + 1
    return False


def bubble_sort(values):
    for _ in range(len(values)):
        swap = False
        for x in range(len(values) - 1): #n-1 as -1 * no of operations = -one pass
            if values[x + 1] < values[x]:
                swap = True
                values[x], values[x + 1] = values[x + 1], values[x]
        if swap == False:
            break
    return values

print(bubble_sort([1434,5,5,344252,3523,523,4,234,324,234,234,23]))

#Number of passes required
#2 
#12354 -> 12345 | 12345 -> 12345 (check) therefore 2
#5 passes 
# c  -> 1
def selection_sort(values, sort_order):
    if sort_order == 'A':
        for y in range(len(values) -1): #-1 because no need compare last number 
            minimum = values[y]
            for x in range(y + 1, len(values)): #based on the assumption that the first one is taken already
                if values[minimum] > values[x]:
                    minimum = x
            if y != minimum:
                values[minimum], values[y] = values[y], values[minimum]
    elif sort_order == "B":
        for y in range(len(values) -1): #-1 because no need compare last number 
            minimum = values[y]
            for x in range(y + 1, len(values)): #based on the assumption that the first one is taken already
                if values[minimum] < values[x]:
                    minimum = x
            if y != minimum:
                values[minimum], values[y] = values[y], values[minimum]
    return values




def insertion_sort(values):
    for x in range(1, len(values)):
  
        while x > 0 and values[x - 1] > values[x]:
            values[x], values[x-1] = values[x - 1], values[x] #n-1 as it assumes first is in palce already
            x-=1
    return values

print(insertion_sort([3,1,4,4,2,1,0]))

def summing(x):
    print(x)
    if x == 1:
        return 1
    return x + summing(x - 1)

def sumDigits(n):
    if len(n) == 1:
        return int(n)
    return int(n[0]) + sumDigits(n[1:])
print(sumDigits("2345"))

def palindrome(n):
    if len(n) == 1:
        return True 
    elif n[0] == n[-1]:
        palindrome(n[1:-1])
    else:
        return False


def exprecur(x, n):
    if n == 1:
        return x
    return x * exprecur(x, n - 1)

print(exprecur(2,8))


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))




def binary_search_recur(values, target, low, high):
    mid = (low + high)//2
    print(low, high, mid)
    if high < low:
        return False
    elif values[mid] == target:
        return True
    elif values[mid] > target:
        return binary_search_recur(values, target, low, mid - 1)
    elif values[mid] < target:
        return binary_search_recur(values, target, mid + 1, high)

print(binary_search_recur(c:=[1,2,3,4,5], 5, 0, len(c)))

#3
def arrange_list(values, low, high):
    print(low, high)
    if low == high or low > high:
        return values
    elif values[low] % 2  and not values[high] % 2:
        values[low], values[high] = values[high], values[low]
    return arrange_list(values, low + 1, high-1)

print(arrange_list(b:=[3,3,3,3,34,4,44,4], 0, len(b) - 1))
    
    
#example uisng an example of sorting algrithm, the divide and conquer strategy used in algorithm design
#Divide and conquer recursively breaks down the problem 
#Selection sort etc are in-place algorithms as they don't create a new list or memory when sorting unlike merge sort which merges and creates a complete new list 
class GameEntry:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, entry):
        self._name = entry
    @property
    def score(self):
        return self._score 
    @score.setter
    def score(self, entry):
        self._score = entry
    def __str__(self):
        return f"{self._name}, {self._score}"
    

#max no of high scores
#if it reaches max, if a higher score is reached, it will replace the score
class Scoreboard:
    def __init__(self, capacity = 10):
        self.board = [None] * capacity
        self.n = 0
    def __getitem__(self, k):
        return self.board[k]
    def __str__(self):
        return "\n".join(str(self.board[j]) for j in range(self.n))
    def add(self,entry):
        score = entry.score
        if self.n != 10 or self.board[-1].score < score:
            if self.n < len(self.board):
                self.n +=1
            j = self.n - 1
            while j > 0 and self.board[j-1].score < score:
                
                self.board[j] = self.board[j -1]
                j -= 1
        self.board[j] = entry 
    


board = Scoreboard(5)
for e in (('Rob', 750), ('Mike',1105), ('Rose', 590), ('Jill', 740), ('Jack', 510), ('Anna', 660), ('Paul', 720), ('Bob', 400)):
    ge = GameEntry(e[0], e[1])
    board.add(ge)
    print('After considering {0}, scoreboard is:'.format(ge))
    print(board, "\n")

class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        self.shift = shift
        for x in range(26):
            encoder[x] = chr((x + shift) % 26 + ord("A"))
            decoder[x] = chr((x-shift) % 26 + ord("A"))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self.__transform__(message, self._forward)
    def decrypt(self, secret):
        return self.__transform__(secret, self._backward)
    
    def __transform__(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)
cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
coded = cipher.encrypt(message)
print('Secret: ', coded)
answer = cipher.decrypt(coded)
print('Message:', answer)

class Stack:
    def __init__(self):
        self._items = list()
    def is_empty(self):
        return not len(self._items)
    def __len__(self):
        return len(self._items)
    def peek(self):
        assert not self.is_empty(), "Cannot peek at empty stack"
        return self._items[-1]
    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        return self._items.pop()
    def push(self, item):
        return self._items.append(item)
hoi = Stack()
while (c:=input("Enter a number (Press D to end)")) != "D":
    hoi.push(c)
for x in range(len(hoi)):
    print(hoi.pop())
 
    
while True:
    expression = input("\nEnter a Postfix expression to be evaluated: ")
    tokens = expression.split(" ")
    stack = Stack()
    if tokens[0] == "help" or tokens[0] == "?":
        print("Postfix Evaluator takes in a mathematical expression expressed in postfix notation and evaluates it")
    elif tokens[0] == 'quit' or tokens[0] == 'q':
        break
    else:
        valid = True
        while len(tokens) > 0:
            item = tokens[0]
            del tokens[0]
            if item.isdigit():
                stack.push(int(item))
            elif item == "+":
                if len(stack) > 1:
                    stack.push(stack.pop() + stack.pop())
                else:
                    valid = False
                    break
            elif item == "-":
                if len(stack) > 1:
                    temp = stack.pop()
                    stack.push(temp - stack.pop())
                else:
                    valid = False
                    break
            elif item == '*':
                if len(stack) > 1:
                    
                    stack.push(stack.pop() * stack.pop())
                else:
                    valid = False
                    break
            elif item == "/":
                if len(stack) > 1:
                    temp = stack.pop()
                    stack.push(temp + stack.pop())
                else:
                    valid = False
                    break
            elif item == "^":
                if len(stack) > 1:
                    temp = stack.pop()
                    stack.push(temp ** stack.pop())
                else:
                    valid = False
                    break
        if len(stack) > 1 or len(stack) <= 0:
            valid = False
        

        if valid:
            print(stack.peek())
        else:
            print("error")
