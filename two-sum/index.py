def two_sum(nums, target: int):
    result = []
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            if nums[i] + nums[k] == target:
                result.append(i)
                result.append(k)
                break
    return result


print(two_sum(nums=[2, 7, 11, 15], target=9))
