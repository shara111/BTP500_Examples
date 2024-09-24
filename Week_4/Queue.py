from Linked_List import *

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()
        self.tail = None  # Keep track of the last node for efficient enqueue

    def enqueue(self, data):
        '''Add an element to the end of the queue.'''
        new_node = Node(data)
        if self.linked_list.is_empty():
            self.linked_list.push(data)
            self.tail = new_node  # Set tail for the first element
        else:
            self.tail.next = new_node  # Link the new node to the last node
            self.tail = new_node  # Update the tail to the new node
        self.linked_list.size += 1

    def dequeue(self):
        '''Remove the front element from the queue.'''
        if self.linked_list.is_empty():
            return None
        front_data = self.linked_list.pop()
        if self.linked_list.is_empty():
            self.tail = None  # Reset tail if the queue is empty
        return front_data

    def peek(self):
        '''Return the front element without removing it.'''
        if self.linked_list.is_empty():
            return None
        return self.linked_list.sentinel.next.data  # Return data of the first real node

    def is_empty(self):
        '''Check if the queue is empty.'''
        return self.linked_list.is_empty()

    def display(self):
        '''Display the elements in the queue.'''
        print("Queue:", end=" ")
        self.linked_list.display()


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