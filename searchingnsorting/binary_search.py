def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        mid_index = (begin_index + end_index) // 2


        if item == sequence[mid_index]:
            return mid_index
        elif item < sequence[mid_index]:
            end_index = mid_index - 1;
        else:
            begin_index = mid_index + 1;
    return None


# Test the function
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 4

print(binary_search(sequence, item))