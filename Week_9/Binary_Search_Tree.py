import queue
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
    
    def remove(self, data):
        # Base case: we need to find the node first
        if not self:
            return self
        # Case 1: Find the node and remove it
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.remove(data)
        else:
            # Case 2: The node to delete is found
            
            # Case 2.1: Node has no children (leaf node)
            if not self.left and not self.right:
                return None
            
            # Case 2.2: Node has only one child
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            
            # Case 2.3: Node has two children
            # Find the inorder successor (smallest node in the right subtree)
            min_larger_node = self.right.find_min()
            # Replace the current node's data with the inorder successor's data
            self.data = min_larger_node.data
            # Now delete the inorder successor node
            self.right = self.right.remove(self.data)
        
        return self

    def find_min(self):
        '''Helper function to find the minimum value in the right subtree'''
        current = self
        while current.left:
            current = current.left
        return current

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
    
    def find_height(self):
        '''Finds the maximum depth of the tree'''
        value = 0
        if self.data:
            left, right = 0, 0
            if self.left:
                left = self.left.find_height()
            if self.right:
                right = self.right.find_height()
            value = (right if right > left else left) + 1
        return value

    #-----Printing Functions------
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

    def post_order_print(self):
        '''Prints values from smallest to largest, node data is last.'''
        # Will only print things if something's there
        if self.data:
            if self.left:
                self.left.inorder_print()
            if self.right:
                self.right.inorder_print()
            print(self.data, end = " ")
    
    def breadth_first_print(self):
        '''Cathy's implementation, modified for this data structure.'''
        the_nodes = queue.Queue()

        if self.data:
            the_nodes.put(self)

        while not the_nodes.empty():
            curr = the_nodes.get()

            if curr.left:
                the_nodes.put(curr.left)
            if curr.right:
                the_nodes.put(curr.right)

            print(curr.data, end=" ")

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

    bst.remove(3)
    bst.print_tree("")

    print("Printing the BST with breadth first...")
    bst.breadth_first_print()
    print()

    print("Printing the BST in order...")
    bst.inorder_print()
    print()

    print("Printing the BST pre-ordered...")
    bst.pre_order_print()
    print()

    print(f"The height (max depth) of this tree is: {bst.find_height()}")