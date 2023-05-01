def two_sum(nums, target: int):
    result = []
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            if nums[i] + nums[k] == target:
                result.append(i)
                result.append(k)
                break
    return result


def two_sum_pntr(nums, target):
    result = []
    slow = 0
    fast = 1
    while slow < len(nums) - 1:
        if nums[slow] + nums[fast] == target:
            result.append(slow)
            result.append(fast)
            break
        fast += 1
        if fast == len(nums) - 1:
            slow += 1
            fast = slow + 1
    return result


print(two_sum_pntr(nums=[12, 36, 14, 2, 22, 11, 14, 13, 12, 19, 3, 4, 2, 7, 11, 15], target=9))
