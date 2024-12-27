def bubble_sort(nums):
    for i in range(len(nums) -1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp 

nums = [5, 3, 6, 4, 2, 7]

bubble_sort(nums)
print(nums)