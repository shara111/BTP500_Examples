from Linked_List import *

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, data):
        '''Add an element to the end of the queue.'''
        new_node = Node(data)
        self.linked_list.push(data)

    def dequeue(self):
        '''Remove the front element from the queue.'''
        if self.linked_list.is_empty():
            return None
        front_data = self.linked_list.pop() 
        return front_data

    def peek(self):
        '''Return the front element without removing it.'''
        if self.linked_list.is_empty():
            return None
        return self.linked_list.start.next.data  # Return data of the first real node

    def is_empty(self):
        '''Check if the queue is empty.'''
        return self.linked_list.is_empty()

    def display(self):
        '''Display the elements in the queue.'''
        print("Queue:", end=" ")
        self.linked_list.display()
        print()


if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements into the queue
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("After enqueueing elements:")
    queue.display()

    # Peek at the front element
    front_element = queue.peek()
    print(f"Front element: {front_element}")
    
    # Dequeue an element
    dequeued = queue.dequeue()
    print(f"Dequeued element: {dequeued}")
    
    print("After dequeuing an element:")
    queue.display()
    
    # Check if the queue is empty
    empty_check = queue.is_empty()
    print(f"Is the queue empty? {empty_check}")