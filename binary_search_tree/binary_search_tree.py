import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        # if the value passed in is less than self.value, go left
        if value < self.value:
            # if there is nothing in the left side
            if not self.left:
                # add to left using recursion
                self.left = BinarySearchTree(value)
            # if there is something to the left, add it to the next left using recursion
            else:
                self.left.insert(value)
        # if the value passed in is greater than self.value, go right
        else:
            # if there is nothing to the right side
            if not self.right:
                # add to right using recursion
                self.right = BinarySearchTree(value)
            # if there is something to the right, add it to the next right using recursion
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if self.value is already the target
        if self.value == target:
            return True
        
        # if the target is less than self.value, go left
        if target < self.value:
            # if there's no more left, return False
            if not self.left:
                return False
            # else keep going using recursion
            else:
                return self.left.contains(target)
        # if the target is more than self.value, go right
        else:
            # if there is no more right, return False
            if not self.right:
                return False
            # else keep going using recursion
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if you can't go right anymore, return the value
        if not self.right:
            return self.value
        # else keep going right, using recursion
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack.push(node)
        while self.stack.len() > 0:
            popped = self.stack.pop()
            print(popped.value)
            if popped.left:
                self.stack.push(popped.left)

            if popped.right:
                self.stack.push(popped.right)
        return


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
