
def merge_sort(arr):
    if len(arr) > 1:
        #divide
        left_arr = arr[:len(arr) //2] #goes from beginning to the middle of the array
        right_arr = arr[len(arr) // 2:] #goes from the middle to the end of the array

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 #left array index
        j = 0 #right array index
        k = 0 #merge array index
        while i < len(left_arr) and j < len(right_arr): 
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        #Copy remaining elements from the left array (if any)
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        #Copy remaining elements from the right array (if any)
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [2, 3, 4, 5, 6, 7, 8, 8, 9, 2, 3, 4]
merge_sort(arr_test)
print(arr_test)