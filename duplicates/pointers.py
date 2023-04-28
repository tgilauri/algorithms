def remove_duplicates(nums):
    result = []
    for n in nums:
        if not result or n > result[-1]:
            result.append(n)
    return result + ['_'] * (len(nums) - len(result))


def removeDuplicates(nums):
    pntr_slow = 1  # позиция, на котрую мы ставим новое значение
    for pntr_fast in range(1, len(nums)):
        if nums[pntr_fast] > nums[pntr_fast - 1]:
            nums[pntr_slow] = nums[pntr_fast]
            pntr_slow += 1
    for pntr_slow in range(pntr_slow, len(nums)):
        nums[pntr_slow] = "_"
    return nums


print(removeDuplicates([0, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 6]))
print(remove_duplicates([]))
print(remove_duplicates([1]))
