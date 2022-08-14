class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self.items.pop()

    # Return the top item on the stack
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.items[len(self.items)-1]

    # Push an item onto the top of the stack
    def size(self):
        return len(self.items)

# Test Code
stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(list(map(lambda a:a,stack.items)))
print(stack.pop())
print(list(map(lambda a:a,stack.items)))

Prompt = f"Enter a Number (cltr-D to end): "

value = int(input(Prompt))
while True:
    try:
        stack.push(value)
        value = int(input(Prompt))
    except EOFError:
        break
print(f"\nSize Of Stack {len(stack.items)}")
print(f"\nPeek Of Stack {stack.peek()}")
print("\nThe Contents of the Stack:")
while not stack.isEmpty():
    value = stack.pop()
    print(value)
        