from Binary_Tree import *
'''
Here, we're implementing the heapify function.
We'll be calling it on a binary tree which may not
already be max heap style. That way, we can picture the
ideas better. 

Based off of the diagram implementation from these notes:
https://seneca-ictoer.github.io/data-structures-and-algorithms/I-Heaps/heap-sort
'''

def heapify(a_node):
    '''Creates a max heapified version of a binary tree.'''
    if a_node.children:
        largest_child = (max(a_node.children, key=lambda n: n.data))
        largest = (largest_child if largest_child.data > a_node.data else a_node)

        # If largest is not root, swap and continue heapifying
        if largest != a_node:
            # Swap data only, want to keep structure the same
            heapify(largest) # Sift it to the top
            a_node.data, largest.data = largest.data, a_node.data

        # Ensure all children are heapified as well
        for child in a_node.children:
            heapify(child)


if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.add_node(8)
    tree.add_node(7)
    tree.add_node(9)
    tree.add_node(4)
    tree.add_node(-1)
    tree.add_node(10)
    tree.add_node(11)
    tree.display()
    print("---------------------------------------")

    heapify(tree.root)
    tree.display()