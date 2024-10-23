'''
This is a Python implementation of BST. I actually have a C++ 
version on my GitHub already: 
https://github.com/cassLaffan/CPP_Binary_Tree

I've flattened the data structure to just a recursively defined BST;
As in, every sub tree in a BST is also a BST (just like in my C++
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
        '''Prints values from smallest to largest.'''
        # Will only print things if something's there
        if self.data:
            if self.left:
                self.left.inorder_print()
            print(self.data, end = " ")
            if self.right:
                self.right.inorder_print()

    def pre_order_print(self):
        '''Prints values from smallest to largest, node data is first.'''
        # Will only print things if something's there
        if self.data:
            print(self.data, end = " ")
            if self.left:
                self.left.inorder_print()
            if self.right:
                self.right.inorder_print()

    def print_tree(self, prefix, is_left=False):
        '''Prints a string representation of the actual tree.'''
        if self.data:
            print(prefix, end="")
            print("|__" if is_left else "|---", end="")
            print(self.data)
            # Enter the next tree level - left and right branch
            if self.left:
                self.left.print_tree(prefix + ("|   " if is_left else "    "), True)
            if self.right:
                self.right.print_tree(prefix + ("|   " if is_left else "    "), False)

if __name__ == "__main__":
    bst = BST(6)
    bst.insert(7)
    bst.insert(10)
    bst.insert(1)
    bst.insert(3)
    bst.insert(-4)
    bst.insert(19)

    bst.print_tree("")

    print(f"Is 10 in the our BST? {bst.search(10)}")
    print(f"Is -1 in the our BST? {bst.search(-1)}")

    print("Printing the BST in order...")
    bst.inorder_print()
    print()

    print("Printing the BST pre-ordered...")
    bst.pre_order_print()
    print()