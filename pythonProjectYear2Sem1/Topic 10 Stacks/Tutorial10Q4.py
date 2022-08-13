import Stack as stack

def recEmptyStack(S):
    if S.isEmpty():
        return True
    else:
        S.pop()
        return recEmptyStack(S)

# test code

S = stack.stack()

for i in range(10,60,10):
    S.push(i)

print("Before")
print("S:",S.peekList())

recEmptyStack(S)

print("After") 
print("S:",S.peekList())