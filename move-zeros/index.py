def move_zeros(nums):
    low = 0
    for high in range(len(nums)):
        if nums[high] != 0:
            nums[high], nums[low] = nums[low], nums[high]
            low += 1

    return nums


print(move_zeros([1, 2, 0, 4, 5, 0, 0, 7, 0, 8, 0, 9]))
