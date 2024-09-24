from Linked_List import *

class LinkedListIterator:
    def __init__(self, linked_list):
        self.current = linked_list.sentinel.next  # Start at the first real node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


if __name__ == "__main__":
    # Seriously name things better than me
    ll = LinkedList()
    
    # Push some stuff into the linked list
    ll.push(10)
    ll.push(20)
    ll.push(30)

    print("Linked List:")
    ll.display() 
    
    # Using the LinkedListIterator
    print("Iterating through the linked list:")
    for data in LinkedListIterator(ll):
        print(data)
