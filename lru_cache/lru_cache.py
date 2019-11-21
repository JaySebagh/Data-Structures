import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.capacity = 0
        self.limit = limit
        self.kv_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.kv_dict:
            grab = self.kv_dict[key]
            self.storage.move_to_end(grab)
            return grab.value[1]
        else:
            return None
        
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key exists, update it's value and make it the tail
        if key in self.kv_dict:
            grab = self.kv_dict[key]
            self.storage.move_to_end(grab)
            self.storage.remove_from_tail()
            self.storage.add_to_tail((key, value))
            self.kv_dict[key] = self.storage.tail
        # check if capacity is less than 10
        elif self.capacity < self.limit:
            # if the storage is empty, add the key value as the head
            if self.storage.length < 1:
                self.storage.add_to_head((key, value))
                self.kv_dict[key] = self.storage.head
                self.capacity += 1
                # print(self.kv_dict[key].value)
            # if the capacity is 1, add the key value as the tail
            elif self.storage.length >= 1:
                self.storage.add_to_tail((key, value))
                self.kv_dict[key] = self.storage.tail
                self.capacity += 1
            # if the capacity is greater than 2 and less than 10, add key value as the tail
        # if the capacity is greater than 10, remove the head and add the key value as the tail
        # if I remove the head, does the 2nd node automatically become the new head? Or do I have to reassign?
        else:
            fill_key = self.storage.remove_from_head()
            # print("fill key: ", fill_key)
            self.kv_dict.pop(fill_key[0])
            self.storage.add_to_tail((key, value))
            self.kv_dict[key] = self.storage.tail