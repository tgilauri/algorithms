def remove_duplicates(nums):
    slow = 0
    fast = 1
    while fast <= len(nums):
        if fast >= len(nums):
            result.append(nums[slow])
            break
        if nums[slow] == nums[fast]:
            nums[fast] = None
            fast += 1
            continue

        result.append(nums[slow])
        slow = fast
        fast += 1
    return result


print(remove_duplicates([0, 0, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5]))
