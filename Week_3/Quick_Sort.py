'''
Finally, let's look at quick sort! On average we can compare it
to merge sort, but quick sort runs the rise of being O(n^2)
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Choose a pivot element
    pivot = arr[len(arr) // 2]
    # Partition the list into elements
    # less than and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively apply quick sort to the partitions
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
