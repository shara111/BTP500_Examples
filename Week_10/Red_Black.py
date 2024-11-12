import queue

class RedBlackTree:
    # Red-Black Node colors
    RED = 0
    BLACK = 1

    def __init__(self, data=None):
        '''Initialize the node with data, set left/right children to None, and color to RED by default.'''
        self.data = data
        self.left = None
        self.right = None
        self.color = self.RED  # New nodes are always red by default
        self.parent = None

    def left_rotate(self):
        '''Perform left rotation on the current node to balance the tree.'''
        new_root = self.right
        if new_root.left:
            self.right = new_root.left
            new_root.left.parent = self
        
        new_root.parent = self.parent
        if not self.parent:
            # If no parent, this becomes the root of the tree
            return new_root
        
        if self == self.parent.left:
            self.parent.left = new_root
        else:
            self.parent.right = new_root
        
        new_root.left = self
        self.parent = new_root

        return new_root

    def right_rotate(self):
        '''Perform right rotation on the current node to balance the tree.'''
        new_root = self.left
        self.left = new_root.right
        if new_root.right:
            new_root.right.parent = self
        
        new_root.parent = self.parent
        if not self.parent:
            # If no parent, this becomes the root of the tree
            return new_root
        
        if self == self.parent.right:
            self.parent.right = new_root
        else:
            self.parent.left = new_root
        
        new_root.right = self
        self.parent = new_root

        return new_root

    def insert(self, data):
        '''Insert a node into the Red-Black tree and rebalance if necessary.'''
        if self.data is None:
            # If the tree is empty, make this node the root
            self.data = data
            self.color = RedBlackTree.BLACK  # Root must always be black
            return self

        # Find the correct place to insert the new node
        current = self
        parent = None
        while current:
            parent = current
            if data < current.data:
                if not current.left:
                    current.left = RedBlackTree(data)
                    current.left.parent = current
                    break
                current = current.left
            elif data > current.data:
                if not current.right:
                    current.right = RedBlackTree(data)
                    current.right.parent = current
                    break
                current = current.right
            else:
                # If the data is already in the tree, do not insert it again
                return self

        # Now that the node has been inserted, fix any Red-Black tree violations
        self.fix_insert(current.left if current.left and current.left.data == data else current.right)

        return self

    def fix_insert(self, node):
        '''Fix the Red-Black Tree properties after insertion.'''
        while node != self and node.parent and node.parent.color == RedBlackTree.RED:
            if not node.parent.parent or node.parent.parent.color:
                break
            elif node.parent == node.parent.parent.left:
                # Case 1: Uncle is red
                uncle = node.parent.parent.right
                if uncle and uncle.color == RedBlackTree.RED:
                    node.parent.color = RedBlackTree.BLACK
                    uncle.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    node = node.parent.parent
                else:
                    # Case 2: Node is right child
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate()
                    # Case 3: Node is left child
                    node.parent.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    self.right_rotate()
            else:
                # Mirror of the above case (for the right child of the grandparent)
                uncle = node.parent.parent.left
                if uncle and uncle.color == RedBlackTree.RED:
                    node.parent.color = RedBlackTree.BLACK
                    uncle.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate()
                    node.parent.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    self.left_rotate()

        # Ensure the root is always black
        self.color = RedBlackTree.BLACK

    def search(self, data):
        '''Search for a node with the given value.'''
        current = self
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def find_height(self):
        '''Find the maximum depth (height) of the tree.'''
        height = 0
        if self.data:
            # Get the height of the left and right subtrees
            left_height = self.left.find_height() if self.left else 0
            right_height = self.right.find_height() if self.right else 0
            
            # The height of the current tree is the max of its left and right subtrees + 1
            height = 1 + max(left_height, right_height)
        
        return height

    def min_value_node(self):
        '''Return the node with the minimum value found in the tree.'''
        current = self
        while current.left:
            current = current.left
        return current
    
    def delete(self, data):
        '''Delete a node from the Red-Black Tree and rebalance if necessary.'''
        if not self:
            return self  # If the tree is empty, return None

        # Step 1: Perform standard BST delete operation
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # Node to be deleted found
            if not self.left or not self.right:
                # Case 1: Node has one child or no child
                temp = self.left if self.left else self.right
                return temp  # Return the non-null child or None if no child
            else:
                # Case 2: Node has two children, get the inorder successor (smallest in the right subtree)
                temp = self.right.min_value_node()
                self.data = temp.data  # Copy the inorder successor's value to this node
                self.right = self.right.delete(temp.data)  # Delete the inorder successor

        return self

    # Printing Functions
    def inorder_print(self):
        '''Prints values from smallest to largest.'''
        if self.data:
            if self.left:
                self.left.inorder_print()
            print(self.data, end=" ")
            if self.right:
                self.right.inorder_print()

    def pre_order_print(self):
        '''Prints values from smallest to largest, node data is first.'''
        if self.data:
            print(self.data, end=" ")
            if self.left:
                self.left.inorder_print()
            if self.right:
                self.right.inorder_print()

    def post_order_print(self):
        '''Prints values from smallest to largest, node data is last.'''
        if self.data:
            if self.left:
                self.left.inorder_print()
            if self.right:
                self.right.inorder_print()
            print(self.data, end=" ")
    
    def breadth_first_print(self):
        '''Breadth-First search print.'''
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
        '''Prints a string representation of the tree structure'''
        if self.data:
            print(prefix, end="")
            print("|__" if is_left else "|---", end="")
            print(self.data)
            
            if self.left:
                self.left.print_tree(prefix + ("|   " if is_left else "    "), True)
            if self.right:
                self.right.print_tree(prefix + ("|   " if is_left else "    "), False)


# Testing the Red-Black Tree
if __name__ == "__main__":
    rbt = RedBlackTree()
    rbt.insert(6)
    rbt.insert(7)
    rbt.insert(10)
    rbt.insert(1)
    rbt.insert(3)
    rbt.insert(-4)
    rbt.insert(19)

    rbt.print_tree("", is_left=False)

    print(f"Is 10 in the our Red-Black Tree? {rbt.search(10)}")
    print(f"Is -1 in the our Red-Black Tree? {rbt.search(-1)}")

    print(f"The height (max depth) of this tree is: {rbt.find_height()}")

    rbt.delete(3)
    rbt.print_tree("", is_left=False)
