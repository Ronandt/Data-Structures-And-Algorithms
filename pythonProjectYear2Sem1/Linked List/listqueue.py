# The storage class for creating the linked list nodes
class QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None


# Implementation of the Queue ADT using a linked list
class Queue:
    # Creates an empty queue.
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0


# Returns True if the queue is empty

def isEmpty(self):
    return self._qhead is None


# Returns the number of items in the queue

def __len__(self):
    return self._count


# Adds the given item to the queue.
def enqueue(self, item):
    node = QueueNode(item)
    if self.isEmpty():
        self._qhead = node
    else:
        self._qtail.next = node
        self._qtail = node
        self._count += 1


# Removes and returns the first item in the queue
def dequeue(self):
    assert not self.isEmpty(), "Cannot dequeue from an empty queue."
    node = self._qhead
    if self._qhead is self._qtail:
        self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item

    # Return the content of the Queue linked list for Print ()
    def __str__(self):
        outStr = ''
        node = self._qhead
        while node is not None:
            outStr += str(node.item) + " "
            node = node.next
        return outStr


# Test code
if __name__ == '__main__':
    myQL = Queue()
    for i in range(10, 60, 10):
        myQL.enqueue(i)
    print("Queue content : ", myQL, "\n")
    myQL.dequeue()
    print("Queue content : ", myQL, "\n")
