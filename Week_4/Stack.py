from Linked_List import *

'''
Now, let's make a stack based off of the Linked List implemented
in the other file.
'''

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, data):
        '''Push an element onto the stack.'''
        self.linked_list.push(data)

    def pop(self):
        '''Pop the top element off the stack.'''
        return self.linked_list.pop()

    def peek(self):
        '''Return the top element without removing it.'''
        return self.linked_list.peek()

    def is_empty(self):
        '''Check if the stack is empty.'''
        return self.linked_list.is_empty()

    def display(self):
        '''Display the elements in the stack.'''
        current = self.linked_list.sentinel.next
        print("Stack:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    # An aptly named stack
    stack = Stack()

    # Push some elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("After pushing elements:")
    stack.display()

    # Take a peek at the top element
    top_element = stack.peek()
    print(f"Top element: {top_element}")

    # Pop an element
    popped = stack.pop()
    print(f"Popped element: {popped}") 

    print("After popping an element:")
    stack.display()

    # Check if the stack is empty (it's not)
    empty_check = stack.is_empty()
    print(f"Is the stack empty? {empty_check}") 