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

    def peekList(self):
        return self.items

