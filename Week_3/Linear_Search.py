'''
An example implementation of linear search!
Notice how I still observe one entry, one exit?
'''
# Runs in linear time! Remember, worst case is if
# every element is checked (the answer is at the end
# or there is no element in the array matching the query)
def linear_search(arr, target):
    loc = -1
    for index, element in enumerate(arr):
        if element == target:
            loc = index
    return loc

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50]
    target = 30
    print(linear_search(arr, target)) # Output is 2!

    new_arr = [40, 10, 20, 50, 30]
    target = 50
    print(linear_search(new_arr, target)) # Output is 3!
