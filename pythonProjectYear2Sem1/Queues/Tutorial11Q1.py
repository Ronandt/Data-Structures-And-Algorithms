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

# The Contents of the queue:
#  [0]:0 [1]:3 [2]:6 [3]:9 [4]:12 [5]:15
print("Part A")
print(myQueue.listQueue())
# (b)
myQueue = Queue()
for i in range( 16 ):
    if i % 3 == 0:
        myQueue.enqueue(i)
    elif i % 4 == 0:
        myQueue.dequeue()
print("Part B")
print(myQueue.listQueue())
# The Contents of the queue:
#  [0]:6 [1]:9 [2]:12 [3]:15
myQueue = Queue()
for i in range( 16 ):
    if i % 3 == 0:
        myQueue.enqueue(i)
        myQueue.enqueue(i + 1)
    elif i % 4 == 0:
        myQueue.dequeue()
print("Part C")
print(myQueue.listQueue())
# (c)
# The Contents of the queue:
#  [0]:3 [1]:4 [2]:6 [3]:7 [4]:9 [5]:10 [6]:12 [7]:13 [8]:15 [9]:16
myQueue = Queue()
for i in range( 16 ):
    if i % 4 == 0:
        myQueue.dequeue()
    elif i % 3 == 0:
        myQueue.enqueue(i)

# The Contents of the queue:
#  Cannot dequeue from an empty queue" AssertionError
print("Part D")
print(myQueue.listQueue())