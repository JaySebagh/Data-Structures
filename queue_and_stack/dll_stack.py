import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.length < 1:
            return None
        removed = self.storage.remove_from_tail()
        return removed

    def len(self):
        return self.storage.length
