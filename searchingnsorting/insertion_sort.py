#PseudoCOde
#Iterate through the array from the second element
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i] #The element to be inserted
        position = i #start at the current index

        #Compare the current value with elements in the sorted part of the array
        while position > 0 and arr[position -1] > current_value:
            arr[position] = arr[position -1] #shift element to the right
            position -= 1 #move to the left

        #Insert the current value into its correct position
        arr[position] = current_value