# For a singly linked-list with only a head reference, appending a new node to the list
# requires linear time since a complete traversal is required to reach the end of the list.
# Instead of a single head reference, a singly linked list can have two external references,
# one for the head and one for the tail. The figure below shows a sample linked list
# using both a head and a tail reference:


# Based on the description given above:
# a. Write a Python function that appends a node to a singly linked list that has both a
# head and a tail reference.
# b. Write a Python function that removes a target node from a singly linked list that has
# both a head and a tail reference


# Part A Solution

# Given the head and tail pointers, adds an item to a linked list.
newNode = ListNode(item)
if head is None:
    head = newNode
else:
    tail.next = newNode
    tail = newNode



# Part B Solution
# Given the head and tail references, removes a target from a
# linked list.
predNode = None
curNode = head
while curNode is not None and curNode.data != target:
    predNode = curNode
    curNode = curNode.next

if curNode is not None:
    if curNode is head:
        head = curNode.next
    else:
        predNode.next = curNode.next
    if curNode is tail:
        tail = predNode