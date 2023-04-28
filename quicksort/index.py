def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = int(len(arr) / 2)
    lower = [item for idx, item in enumerate(arr) if item < arr[pivot] and idx != pivot]
    greater = [item for idx, item in enumerate(arr) if item > arr[pivot] and idx != pivot]

    return quicksort(lower) + [arr[pivot]] + quicksort(greater)


print(quicksort([1, 3, 35, 28, 9, 4, 8, 2, 7, 6, 5, 11,10,15,22,25,19,13]))
