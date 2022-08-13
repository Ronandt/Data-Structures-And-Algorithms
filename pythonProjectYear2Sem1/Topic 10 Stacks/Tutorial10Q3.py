import Stack as stack

def transfer (S,T):
    while not S.isEmpty():
        T.push(S.pop())

# Test Code
S = stack.stack()
T = stack.stack()

for i in range(10,60,10):
    S.push(i)

print("Before")
print("S:",S.peekList())
print("T:",T.peekList())

transfer(S,T)

print("After")
print("S:",S.peekList())
print("T:",T.peekList())