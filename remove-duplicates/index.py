def remove_duplicates(nums):
    pntr_slow = 1  # позиция, на котрую мы ставим новое значение
    for pntr_fast in range(1, len(nums)):
        # записываем только элементы, которые больше, чем предыдущие, т.е. уникальные
        if nums[pntr_fast] > nums[pntr_fast - 1]:
            nums[pntr_slow] = nums[pntr_fast]
            pntr_slow += 1
    # остаток добиваем подчеркиваниями
    for pntr_slow in range(pntr_slow, len(nums)):
        nums[pntr_slow] = "_"
    return nums


print(remove_duplicates([0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9]))
