'''
Let's look at an implementation of bubble sort!
'''
# Let's assume arr's len is 5
def bubble_sort(arr):
    n = len(arr) # 1 
    # Bubbles up the list
    for i in range(n): # n
        for j in range(0, n-i-1): # n ^2
            # Checks if the items are out of order
            if arr[j] > arr[j+1]: # 
                # Switches them
                arr[j], arr[j+1] = arr[j+1], arr[j] #

# T(n) = 1 + n + (n-1) + (n - 2) + (n - 3) + .... + (n - (n-1)) -> n^2

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print(arr)
