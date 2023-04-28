def group_range(nums):
    result = []
    numbers = sorted(nums)
    last_group_start = None
    last_group_end = None

    for n in list(numbers) + [None]:
        if last_group_start is None:
            last_group_start = n
        if last_group_end is None:
            last_group_end = n

        if n is not None:
            if last_group_end == n - 1:
                last_group_end = n

        if n is None or n > (last_group_end + 1):
            if last_group_start == last_group_end:
                result.append(f"{last_group_end}")
            else:
                result.append(f"{last_group_start}-{last_group_end}")
            last_group_start = n
            last_group_end = n

    return ','.join(result)


print(group_range([1, 4, 5, 2, 3, 9, 8, 11, 0]))
print(group_range([1, 4, 3, 2]))
print(group_range([1, 4]))
print(group_range([1, 4, 5, 8, 9, 7, 12, 16, 21, 25, 23, 24, 22, 6]))
