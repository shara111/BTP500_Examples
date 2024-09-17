'''
This file will demonstrate some examples of where mutability
vs. immutability come into play now that we know Python
passes by reference.
'''

# Recall that numerical literals are immutable
def modify_int(x):
    x += 1
    return x

# Recall that lists are mutable!
def modify_list(lst):
    lst.append(4)


if __name__ == '__main__':
    a = 5
    b = modify_int(a)
    print(a)  # Output: 5 (original value unchanged)
    print(b)  # Output: 6 (new value returned)

    c = [1, 2, 3]
    modify_list(c)
    print(c)  # Output: [1, 2, 3, 4] (original list modified)