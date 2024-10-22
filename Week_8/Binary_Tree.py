import random
'''
This is a binary tree implementation. Nodes
can have zero, one or two children.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.children = [] # Cannot be more than two elements

    def add_node(self, data):
        if len(self.children) < 2:
            self.children.append(Node(data))
            self.children.sort(key=lambda n: n.data) # Just so they're in order
        else:
            if data < self.children[0].data:
                self.children[0].add_node(data)
            elif data > self.children[1].data:
                self.children[1].add_node(data)
            else:
                return # do nothing as the node already exists in the tree

    def display(self, level=0, prefix=""):
        # Print the current node with prefix for the connection
        print(prefix + f"{self.data}")
        
        # Prepare the prefix for children
        if self.children:
            # Set the prefix for the first child
            child_prefix = prefix + "    "
            
            # Iterate through children
            for child in self.children:
                child_prefix = prefix + "|  "
                child.display(level + 1, child_prefix)

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def add_node(self, data):
        self.root.add_node(data)

    def display(self):
        self.root.display()

if __name__ == "__main__":
    random.seed(10)
    tree = BinaryTree(5)
    tree.add_node(8)
    tree.add_node(7)
    tree.add_node(9)
    tree.add_node(4)
    tree.add_node(-1)
    tree.add_node(10)
    tree.add_node(11)
    tree.display()