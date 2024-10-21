'''
Here we have a full fledged linked list implementation.
Sentinel nodes and everything!
'''

# A class representing a single node in the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def display(self):
        print(f"{self.data}", end="")
        if self.next:
            print("->", end="")

# Useful for edge cases!
class SentinelNode:
    def __init__(self):
        self.next = None

# Iterator Class
class ListIterator:
    def __init__(self, linked_list):
        self.current = linked_list.start # hehehe

    def __iter__(self):
        return self

    def __next__(self):
        self.current = self.current.next
        if self.current == None:
            raise StopIteration
        return self.current

class LinkedList:
    def __init__(self):
        self.start = SentinelNode() 
        self.end = SentinelNode()
    
    def is_empty(self):
        return self.start.next == None

    def push(self, data):
        '''Insert an element at the beginning of the list.'''
        new_node = Node(data)
        new_node.next = self.start.next
        if self.is_empty():
            self.end.next = new_node
        self.start.next = new_node

    def append(self, data):
        '''Insert an element at the end of the list.'''
        new_node = Node(data)
        if not self.start.next:
            self.start.next = new_node
        if self.end.next:
            self.end.next.next = new_node
        self.end.next = new_node

    def pop(self):
        '''Remove the element from the beginning of the list.'''
        if not self.start.next:
            return None
        popped_node = self.start.next
        self.start.next = popped_node.next
        if self.start.next == None:
            self.end.next = None
        return popped_node.data

    def search(self, key):
        '''Search for an element in the list. Linear search'''
        current = self.start.next
        flag = False
        while current and not flag:
            if current.data == key:
                flag = True
            current = current.next
        return flag

    def display(self):
        '''Display the elements in the list.'''
        for data in iter(self):
            data.display()
    
    def remove(self, element):
        '''Removes a specified element. Linear!'''
        current = self.start.next
        prev = None
        found = False
        while current and not found:
            if current.data == element:
                found = True
            else:
                prev = current
                current = current.next
        if found:
            prev.next = current.next
            return current
        return None
    
    # Iter is short for iterator
    def __iter__(self):
        return ListIterator(self)