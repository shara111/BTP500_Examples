'''
Here, we will define a hash table with chaining!
Chaining is a method of implementing a hash table using
linked lists. Of course, here for brevity we're taking 
advantage of Python's built-in features.

By "brevity" I actually mean I am lazy.
'''

class HashTable:
    def __init__(self):
        # Setting up our hash table with a size of 10
        self.size = 10
        # Creating a list of empty lists (buckets) to store our key-value pairs
        self.table = [[] for _ in range(self.size)]

    # This function turns the key into an index for the table
    def hash_function(self, key):
        return hash(key) % self.size

    # Here’s where we add a new key-value pair to the table
    def insert(self, key, value):
        # Find the index for the key using our hash function
        index = self.hash_function(key)  
        # Add the key-value pair to the correct bucket
        self.table[index].append((key, value))

    # This function lets us look up the value for a given key
    def lookup(self, key):
        # Get the index for the key we're looking for
        index = self.hash_function(key)  
        # Check the bucket for the key
        for k, v in self.table[index]:
            if k == key:  # If we find the key, return its value
                return v
        return None  # If the key isn't found, just return None

if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.insert('key1', 'value1')
    hash_table.insert('key2', 'value2')
    hash_table.insert('key3', 'value3')
    hash_table.insert('key4', 'value4')

    print(hash_table.lookup('key2'))