'''
This file is going to show you how Python's variables are all
passed by reference!
'''

# This applies to both assignment and function calls
def modify_list(lst):
    lst.append(4)

if __name__ == '__main__':
    a = [1, 2, 3]
    b = a  # `b` is now a reference to the same list as `a`
    b.append(4)
    print(a)  # Output: [1, 2, 3, 4]

    c = [1, 2, 3]
    modify_list(c)
    print(c)  # Output: [1, 2, 3, 4]
