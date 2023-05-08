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
    sorted_nums = sorted(nums)
    return two_sum_sorted_pntr(sorted_nums, target)


def two_sum_sorted_pntr(nums, target):
    result = []
    left = 0
    right = len(nums) - 1
    while right > left:
        sum = nums[left] + nums[right]
        if sum == target:
            result.append(nums[left])
            result.append(nums[right])
            break
        if sum < target:
            left += 1
        if sum > target:
            right -= 1
    return result


def two_sum_with_dict(nums, target):
    hash_map = {}

    for i in range(len(nums)):
        num = nums[i]
        if (target - num) in hash_map:
            return [hash_map[target - num], i]
        hash_map[num] = i
    return None


print(two_sum_pntr(nums=[12, 36, 14, 2, 22, 11, 14, 13, 12, 19, 3, 4, 2, 7, 11, 15], target=9))
print(two_sum_sorted_pntr(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=9))
print(two_sum_with_dict(nums=[2, 7, 3, 8, 4, 9, 5, 1], target=12))
