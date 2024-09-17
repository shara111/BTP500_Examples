'''
Here we have an implementation of merge sort! It looks complex
but if you follow the steps and understand what I'm doing at each
step, you should be ok! For more help, check out Cathy's useful
animation: http://cathyatseneca.github.io/DSAnim/web/merge.html
'''

def merge_sort(arr):
    # Obviously we don't want to sort an array of length 1
    if len(arr) > 1:
        mid = len(arr) // 2 # Split the list in half
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively call merge sort on both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Set indicies at starting points
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            # Swap orders depending on the comparisons
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Merge the two sorted halves into a single sorted list
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)
    print(arr)
