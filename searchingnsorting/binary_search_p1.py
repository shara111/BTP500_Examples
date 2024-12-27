# You have a sorted list of numbers:

#python
#Copy code
#array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
#Write a Python function using binary search to find the index of the target number 23. 
#If the number is not found, the function should return -1.

#pseudo code or steps
##1) define the low and the high of a list
#2) after that, we find the middle part of the list
#3) if the target equals middle, we're done
#4) if the target it greater, we do -1
#5) if the target is smaller, we do +1
#6) we repeat the process until we find the target or the list is empty
#7) if the list is empty, we return -1

def binary_search(array, target):
    beginning = 0
    end = len(array) - 1

    while beginning <= end:
        mid = (beginning + end) // 2

        if target == array[mid]:
            return mid
        elif target > array[mid]:
            beginning = mid + 1
        else:
            end = mid - 1
    return -1

#test
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(array, 23))  # Output: 5

