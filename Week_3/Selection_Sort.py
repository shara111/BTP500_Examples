'''
Here we'll be looking at selection sort!
'''

def selection_sort(arr):
    n = len(arr)
    # Outer loop that checks the whole list
    for i in range(n):
        min_index = i # Move the boundary of the sorted portion
        for j in range(i+1, n):
            # Find the minimum unsorted index
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap it with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)
    print(arr)
