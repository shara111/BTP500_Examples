import random
'''
This is a very basic tree implementation. As you can see,
it's just a linked list or special graph. Connections are
directed in trees, and only go down to the children, or the
next tier.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        self.children.append(Node(data))
        self.children.sort(key=lambda n: n.data) # Just so they're in order

    def display(self):
        print(f"{self.data}", end="")
        for child in self.children:
            print("    ->", end="")
            child.display()
        print()

class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def display(self):
        self.root.display()

if __name__ == "__main__":
    random.seed(10)
    tree = Tree(5)
    tree.root.add_child(8)
    tree.root.add_child(7)
    tree.root.add_child(9)
    tree.display()

    for i in range(8, 15):
        rand_int = random.randint(0, len(tree.root.children) - 1)
        tree.root.children[rand_int].add_child(i)
    
    tree.display()