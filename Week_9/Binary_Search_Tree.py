'''
This is a Python implementation of BST. I actually have a C++ 
version on my GitHub already: 
https://github.com/cassLaffan/CPP_Binary_Tree

I've flattened the data structure to just a recursively defined BST;
As in, every sub tree in a BST is also a BST. (Just like in my C++
implementation).

Also everything is recursion here because it's cleaner.
Stack frames be damned!
'''

class BST:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # No data here at root
        if not self.data:
            self.data = data
        # Insert to the left if it's smaller
        elif data < self.data:
            # Gotta check if it exists first
            if not self.left:
                self.left = BST(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            # Same here
            if not self.right:
                self.right = BST(data)
            else:
                self.right.insert(data)
    
    def search(self, data):
        found = False
        # Will only check if the tree exists at all
        if self.data:
            if self.data == data:
                found = True
            # Wasting an extra stack frame for cleaner code
            elif self.data < data and self.right:
                found = self.right.search(data)
            elif self.data > data and self.left:
                found = self.left.search(data)
        return found
    
    def inorder_print(self):
        pass

    def pre_order_print(self):
        pass

    def breadthfirst_print(self):
        pass

if __name__ == "__main__":
    bst = BST(6)
    bst.insert(7)
    bst.insert(10)
    bst.insert(1)
    bst.insert(3)

    print(bst.search(10))
    print(bst.search(-1))
