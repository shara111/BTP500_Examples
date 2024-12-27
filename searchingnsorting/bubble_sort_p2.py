# Write a Python function using Bubble Sort to sort the following list of numbers in ascending order:

# python
# Copy code
# arr = [64, 34, 25, 12, 22, 11, 90]
# Once sorted, your function should return the sorted list.

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+ 1]:
                temp = arr[j]
                arr[j] = arr[j+ 1]
                arr[j + 1] = temp

#test
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)
print(arr) 