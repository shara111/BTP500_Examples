from Linked_List import LinkedList


class LinkedHash:
    def __init__(self):
        self.size = 1
        self.elements = 0
        self.table = [LinkedList() for _ in range(self.size)]
    def hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        # resize. is there an optimum for number of elements vs size
        # for when it should be resized?
        if self.elements + 1 > self.size:
            # double size
            self.size *= 2
            # temporary table
            table2 = [LinkedList() for _ in range(self.size)]
            # remove elements from old table and put into new table
            for ll in self.table:
                element = ll.pop()
                while element is not None:
                    # hash function with doubled size
                    index = self.hash_function(element[0])
                    table2[index].push(element)
                    element = ll.pop()
            # replace old table with new table
            self.table = table2
        # add new element
        index = self.hash_function(key)
        # dict should not contain duplicate keys - overwrite duplicates
        # how does one remove an element from a linked list?
        element = self.table[index].pop()
        if element is None:
            # if no elements in linked list, push new key-value
            self.table[index].push((key, value))
            self.elements += 1
            return
        first_key = element[0]
        while (True):
            if element[0] == key:
                # leave previous key-value removed; add new key-value
                self.table[index].append((key, value))
                return
            # append to back of linked list
            self.table[index].append(element)
            element = self.table[index].pop()
            if element[0] == first_key:
                # looped around - key-value not found. re-add last removed element
                self.table[index].push(element)
                # key-value not found; add to list
                self.table[index].push((key, value))
                self.elements += 1
                return
    def lookup(self, key):
        index = self.hash_function(key)
        for element in self.table[index]:
            if element[0] == key:
                return element[1]
        return None
    def delete(self, key):
        index = self.hash_function(key)
        element = self.table[index].pop()
        if element is None:
            return
        first_key = element[0]
        while (True):
            if element[0] == key:
                # leave removed
                self.elements -= 1
                return
            # append to back of linked list
            self.table[index].append(element)
            element = self.table[index].pop()
            # if looped detected
            if element[0] == first_key:
                # re-add last removed element
                self.table[index].append(element)
                return
    def print(self):
        print ("Contents of linked list hash table:")
        for ll in self.table:
            for element in ll:
                print (str(element[0]) + ": " + str(element[1]) + " -> ", end='')
            print ("None")

if __name__ == "__main__":
    lh = LinkedHash()
    lh.insert('key1', 'value1')
    lh.insert('key2', 'value2')
    lh.insert('key3', 'value3')
    lh.insert('key4', 'value4')
    lh.print()
    print (lh.lookup('key2'))
    lh.insert('key4', 'value44')
    lh.insert('key5', 'value5')
    lh.delete('key2')
    lh.print()
    lh.delete('key1')
    lh.delete('key3')
    lh.delete('key4')
    lh.delete('key5')
    lh.print()
    print()
    print ("insert 100 different elements")
    for i in range(100):
        lh.insert(str(i), i)
    print ("Size: ", lh.size)
    print()
    print ("lookup all 100 elements")
    for i in range(100):
        if lh.lookup(str(i)) != i:
            print ("Error! " + i + " not found, or is incorrect!")
            lh.print()
    print()
    print("update all 100 elements")
    for i in range(100):
        lh.insert(str(i), i + 1)
    print ("Size: ", lh.size)
    lh.print()
    print()
    print("lookup all 100 elements again")
    for i in range(100):
        if lh.lookup(str(i)) != i + 1:
            print ("Error! " + i + " not found, or is incorrect!")
            lh.print()
    print()
    print("remove all 100 elements. should now be empty.")
    for i in range(100):
        lh.delete(str(i))
    lh.print()