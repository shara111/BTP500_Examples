from Linked_List import *

'''
A student's implementation of the chaining style
of hash tables; needed a bit of cleaning up because
he opted for a list for buckets. That's fine but it also
removes the necessity of resizing because Python resizes
lists for us.

Really, I took his file and made it lazier, in line with
Python standards.
'''

class LinkedHash:
    def __init__(self):
        self.elements = 0
        self.table = [LinkedList(), LinkedList()]
    
    def hash_function(self, key):
        return hash(key) % (len(self.table))
    
    def insert(self, key, value):
        # If it's full
        if len(self.table) == self.elements:
            # Double its "size"
            for _ in range(len(self.table)):
                self.table.append(LinkedList()) 

        # Index the new element
        index = self.hash_function(key)

        if self.table[index].is_empty():
            self.table[index].append((key, value))
            self.elements += 1
        else:
            # dict should not contain duplicate keys - overwrite duplicates
            for element in self.table[index]:
                if element.data[0] == key:
                    self.table[index].remove(element)
            self.table[index].append((key, value))


    def lookup(self, key):
        index = self.hash_function(key)
        for element in self.table[index]:
            if element.data[0] == key:
                return element.data[1]
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        for element in self.table[index]:
            if element.data[0] == key:
                self.table[index].remove(element)
                return
            
    def print(self):
        print ("Contents of linked list hash table:")
        for ll in self.table:
            ll.display()
            print()

if __name__ == "__main__":
    lh = LinkedHash()
    lh.insert('key1', 'value1')
    lh.insert('key2', 'value2')
    lh.print()

    print(lh.lookup('key2'))
    lh.insert('key4', 'value44')
    lh.insert('key5', 'value5')
    lh.delete('key2')

    lh.delete('key1')
    lh.delete('key3')
    lh.delete('key4')
    lh.delete('key5')
    lh.print()