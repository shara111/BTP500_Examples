'''
Here, we'll put linear probing to use on a hash table.
Linear probing is a way to deal with collisions by simply searching
for the next empty spot, even if that means looping back to the 
front.

Try pulling this code and implementing tombstoning, double hashing
or quadratic probing!
'''

class LinearProbingHashTable:
    def __init__(self):
        # Setting up our hash table with a size of 10
        self.size = 10
        # Creating an empty table filled with None
        self.table = [None] * self.size

    # This function takes a key and turns it into an index for our table
    def hash_function(self, key):
        return hash(key) % self.size

    # Time to add a key-value pair to the table
    # This uses method 1 from the notes, the most basic version
    def insert(self, key, value):
        # Get the initial index for the key
        index = self.hash_function(key)
        # If that spot is taken, keep looking for the next available one
        while self.table[index] is not None:
            index = (index + 1) % self.size  # Wrap around if needed
        # Found an empty spot! Store the key-value pair there
        self.table[index] = (key, value)

    # Let’s look up a value by its key
    def lookup(self, key):
        # Get the starting index for the key
        index = self.hash_function(key)
        # Keep checking until we find the key or hit an empty spot
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Found the key! Return its value
                return self.table[index][1]
            index = (index + 1) % self.size  # Move to the next index
        return None  # If we didn’t find the key, just return None

if __name__ == "__main__":
    hash_table = LinearProbingHashTable() 
    hash_table.insert('key1', 'value1')
    hash_table.insert('key2', 'value2') 
    hash_table.insert('key3', 'value3')

    print(hash_table.lookup('key2'))
