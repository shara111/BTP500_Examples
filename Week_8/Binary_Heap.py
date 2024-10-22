'''
Here I have an implementation of a Binary Heap!
Useful for priority queues and when you need to sift
and order by the priority of something.
'''

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        '''Insert a new value into the heap.'''
        self.heap.append(value)  # Add the new value at the end
        self._bubble_up(len(self.heap) - 1)  # Restore the heap property

    def remove_max(self):
        '''Remove and return the maximum value from the heap.'''
        if not self.heap:
            return None # Can't remove anything from it
        
        max_value = self.heap[0]  # The root is the maximum value
        last_value = self.heap.pop()  # Remove the last value
        
        if self.heap:
            self.heap[0] = last_value  # Move the last value to the root
            self._bubble_down(0)  # Restore the heap property
        
        return max_value

    def peek(self):
        '''Return the maximum value without removing it.'''
        if not self.heap:
            return None # Nothing is there
        return self.heap[0]

    def _bubble_up(self, index):
        '''Restore the heap property by bubbling up the value at index.
        Notice how it kind of looks like binary sort?'''
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Swap
            index = parent_index
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        '''Restore the heap property by bubbling down the value at index.'''
        length = len(self.heap)
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_index = index
            
            # Check if the left child exists and is greater than the current largest
            if left_child_index < length and self.heap[left_child_index] > self.heap[largest_index]:
                largest_index = left_child_index
            
            # Check if the right child exists and is greater than the current largest
            if right_child_index < length and self.heap[right_child_index] > self.heap[largest_index]:
                largest_index = right_child_index
            
            # If the largest is still the current index, we are done
            if largest_index == index:
                break
            
            # Swap and continue bubbling down
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            index = largest_index

    # Utility functions
    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

if __name__ == "__main__":
    heap = BinaryHeap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    heap.insert(15)

    print("Heap:", heap)
    print("Max value:", heap.peek())
    print("Removing max:", heap.remove_max())
    print("Heap after removal:", heap)
