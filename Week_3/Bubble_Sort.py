'''
Let's look at an implementation of bubble sort!
'''

def bubble_sort(arr):
    n = len(arr)
    # Bubbles up the list
    for i in range(n):
        for j in range(0, n-i-1):
            # Checks if the items are out of order
            if arr[j] > arr[j+1]:
                # Switches them
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print(arr)
