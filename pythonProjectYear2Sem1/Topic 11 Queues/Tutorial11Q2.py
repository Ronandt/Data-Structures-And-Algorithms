def reverseQueue(Q):
    return Q[::-1]

# Test Code
class Queue:
    # Creates an empty queue
    def __init__(self):
        self._qList = list()

    # Returns True if the queue is empty
    def isEmpty(self):
        return len(self._qList) == 0

    # Return the number of items in the queue
    def __len__(self):
        return len(self._qList)
    def listQueue(self):
        return self._qList

    # Adds the given item to the queue
    def enqueue(self, item):
        self._qList.append(item)

    # Removes and return the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"

        return self._qList.pop(0)

# import pylistqueue as Queue
import stack as stack
# Q1
#(a)
myQueue = Queue()
for i in range( 16 ):
    if i % 3 == 0:
        myQueue.enqueue(i)
y = myQueue.listQueue()
x = reverseQueue(myQueue.listQueue())
print("Before Reverse")
print(y)
print("After Reverse")
print(x)