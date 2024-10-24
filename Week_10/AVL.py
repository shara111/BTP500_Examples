'''
Augumenting last week's BST such that it will be height balanced,
thus becoming an AVL tree.

A tree is height balanced if for every node within the
tree, the height of its right and left subtrees differ by no
more than one.

In the case of the AVL tree, the balance of a node is calculated:

Node's balance = height of right - height of left
     of node        subtree          subtree
'''

class AVL_Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.balance = 0

    def rebalance_helper(self):
        pass

    def insert(self, data):
        # No data here at root
        if not self.data:
            self.data = data
        # Insert to the left if it's smaller
        elif data < self.data:
            # Gotta check if it exists first
            if not self.left:
                self.left = AVL_Tree(data)
                self.balance -= 1
            else:
                self.left.insert(data)
        elif data > self.data:
            # Same here
            if not self.right:
                self.right = AVL_Tree(data)
                self.balance += 1
            else:
                self.right.insert(data)
        if self.balance >= 1 or self.balance <= -1:
            self.rebalance_helper()
    
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
    avl = AVL_Tree(6)
    avl.insert(7)
    avl.insert(10)
    avl.insert(1)
    avl.insert(3)
    avl.insert(-4)
    avl.insert(19)

    avl.print_tree("")

    print(f"Is 10 in the our AVL Tree? {avl.search(10)}")
    print(f"Is -1 in the our AVL Tree? {avl.search(-1)}")

    print(f"The height (max depth) of this tree is: {avl.find_height()}")