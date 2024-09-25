'''
Here we have a full fledged linked list implementation.
Sentinel nodes and everything!
'''

# A class representing a single node in the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Useful for edge cases!
class SentinelNode:
    def __init__(self):
        self.next = None

# Iterator Class
class ListIterator:
    def __init__(self, linked_list):
        self.current = linked_list.sentinel.next
        self.start = linked_list.sentinel

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration # Well ya gotta stop somehow
        value = self.current.data
        self.current = self.current.next
        return value

class LinkedList:
    def __init__(self):
        self.sentinel = SentinelNode() 
        self.sentinel.next = None
        self.size = 0

    def push(self, data):
        '''Insert an element at the beginning of the list.'''
        new_node = Node(data)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        self.size += 1

    def append(self, data):
        '''Insert an element at the end of the list.'''
        new_node = Node(data)
        last = self.sentinel

        while last.next:
            last = last.next
        last.next = new_node
        self.size += 1

    def pop(self):
        '''Remove the element from the beginning of the list.'''
        if not self.sentinel.next:
            return None
        popped_node = self.sentinel.next
        self.sentinel.next = self.sentinel.next.next
        self.size -= 1
        return popped_node.data

    def search(self, key):
        '''Search for an element in the list. Linear search'''
        current = self.sentinel.next
        flag = False
        while current:
            if current.data == key:
                return flag
            current = current.next
        return flag

    def display(self):
        '''Display the elements in the list.'''
        current = self.sentinel.next
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # Iter is short for iterator
    def __iter__(self):
        return ListIterator(self)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


if __name__ == "__main__":
    # Create a linked list (please don't name your variables
    # as poorly as I do mine)
    ll = LinkedList()
    
    # Push a few elements
    ll.push(10)
    ll.push(20)
    ll.push(30)

    print("After pushing elements:")
    ll.display()

    # Append some more elements
    ll.append(40)
    ll.append(50)

    print("After appending elements:")
    ll.display() 

    # Pop the last element
    popped = ll.pop()
    print(f"Popped element: {popped}") # f string formatting hooray
    
    print("After popping an element:")
    ll.display()

    # Search for 40
    found = ll.search(40)
    print(f"Element 40 found: {found}") 

    not_found = ll.search(100)
    print(f"Element 100 found: {not_found}")

    # Using an iterator
    print("Iterating through the list:")
    for value in ll:
        print(value) 