'''
In this file, we will be looking at insertion sort!
'''

def insertion_sort(arr):
    # Start with the second element
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i - 1
        # Compare the current element with elements in the
        # sorted portion
        while j >= 0 and arr[j] > key:
            # Shift elements to the right to make space
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the current element
        arr[j + 1] = key

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    print(arr)
