import math


def minimum_difference(nums: [int], k: int) -> int:
    nums = sorted(nums)
    left = 0
    right = left + k - 1

    best = math.inf

    while right < len(nums):
        cur = nums[right] - nums[left]

        best = min(best, cur)
        left += 1
        right += 1
    return best


print(minimum_difference([9, 4, 1, 7], 2))
