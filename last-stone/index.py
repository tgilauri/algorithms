import heapq


def last_stone_weight(stones: [int]) -> int:
    heap = list(map(lambda x: -x, stones))
    heapq.heapify(heap)

    while len(heap) >= 2:
        stone_1 = heapq.heappop(heap)
        stone_2 = heapq.heappop(heap)
        result = stone_1 - stone_2
        if result != 0:
            heapq.heappush(heap, result)

    return -heapq.heappop(heap) if len(heap) else 0


def last_stone_sort(stones: [int]) -> int:
    stones.sort()

    while len(stones) >= 2:
        stone_1 = stones.pop(-1)
        stone_2 = stones.pop(-1)
        result = stone_1 - stone_2
        if result != 0:
            stones.append(result)
            stones.sort()

    return stones.pop() if len(stones) else 0


print(last_stone_sort([2, 7, 4, 1, 8, 1]))
