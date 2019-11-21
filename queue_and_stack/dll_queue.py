import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.length < 1:
            return None
        removed = self.storage.remove_from_head()
        return removed

    def len(self):
        return self.storage.length