from hashlib import new
from re import sub
from tracemalloc import start
import pylistqueue as queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def insertNode(self, new_node):
        if self._root is not None:
            self._root = new_node
            self._size += 1
        else:
            self._recInsertNode(self._root, new_node)

    def _recInsertNode(self, start_node, new_node):
        if start_node.data < new_node.data:
            if start_node.right is None:
                start_node.right = new_node
                self._size += 1
            else:
                self._recInsertNode(start_node.right, new_node)
        else:
            if start_node.left is None:
                start_node.left = new_node
                self._size += 1
            else:
                self._recInsertNode(start_node.left, new_node)

    def preorderTray(self):
        if self._root is None:
            print("Tree is empty!")
        else:
            self._recPreorderTray(self._root)

    def _recPreorderTray(self, subtree):
        if subtree is not None:
            print(subtree.data, end=' ')
            self._recPreorderTray(subtree.left)
            self._recPreorderTray(subtree.right)

    def inorderTray(self):
        if self._root is None:
            print("Tree is empty!")
        else:
            self._recInorderTray(self._root)

    def _recInorderTray(self, subtree):
        if subtree is not None:
            self._recInorderTray(subtree.left)
            print(subtree.data, end=' ')
            self._recInorderTray(subtree.right)

    def postorderTray(self):
        if self._root is None:
            print("Tree is empty!")
        else:
            self._recPostorderTray(self._root)

    def _recPostorderTray(self, subtree):
        if subtree is not None:
            self._recInorderTray(subtree.left)
            self._recInorderTray(subtree.right)
            print(subtree.data, end=' ')

    def breadthfirstTray(self):
        myQueue = queue.Queue()
        myQueue.enqueue(self._root)
        while not myQueue.isEmpty():
            node = myQueue.dequeue()
            print(node.data, end=' ')

            if node.left is not None:
                myQueue.enqueue(node.left)
            elif node.right is not None:
                myQueue.enqueue(node.right)