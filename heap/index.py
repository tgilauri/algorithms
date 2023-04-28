import math


class Heap:
    def __init__(self, items):
        self.__create_heap(items)

    def __create_heap(self, items):
        self.heap = items
        self.last_index = len(items) - 1
        for i in range(int(self.last_index / 2) - 1, -1, -1):
            self.heapify(i)

    def heapify(self, idx):
        left = (2 * idx) + 1
        right = (2 * idx) + 2

        largest = idx
        if left > self.last_index and right > self.last_index:
            return
        if left <= self.last_index and self.heap[left] > self.heap[largest]:
            largest = left
        if right <= self.last_index and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            tmp_largest = self.heap[largest]
            self.heap[largest] = self.heap[idx]
            self.heap[idx] = tmp_largest
            self.heapify(largest)

    def increase_key(self, i, value):
        if self.heap[i] > value:
            return
        self.heap[i] = value
        prev_idx = math.ceil((i / 2) - 1)
        while i > 0 and self.heap[prev_idx] < self.heap[i]:
            tmp_prev = self.heap[prev_idx]
            self.heap[prev_idx] = self.heap[i]
            self.heap[i] = tmp_prev
            i = prev_idx
            prev_idx = math.ceil((i / 2) - 1)

    def insert(self, val):
        self.heap.append(-math.inf)
        self.last_index += 1
        self.increase_key(len(self.heap) - 1, val)

    def is_empty(self):
        return len(self.heap) == 0

    def get_max(self):
        if len(self.heap) == 0:
            return None
        self.heap[0], self.heap[self.last_index] = self.heap[self.last_index], self.heap[0]
        self.last_index -= 1
        max_el = self.heap.pop()
        self.heapify(0)
        return max_el

    def __str__(self):
        return f"[{', '.join(map(lambda x: str(x), self.heap))}]"

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, item):
        return self.heap[item]

    def __setitem__(self, key, value):
        self.heap[key] = value


heap = Heap([100, 25, 36, 17, 9, 7, 4, 2, 11, 16, 12])

heap.insert(37)
heap.insert(3)
heap.insert(101)

print(heap.get_max())
print(heap)


def heap_sort(items):
    _heap = Heap(items)
    for i in range(_heap.last_index, -1, -1):
        _heap[0], _heap[i] = _heap[i], _heap[0]
        _heap.last_index -= 1
        _heap.heapify(0)
    print(_heap)


heap_sort([100, 25, 36, 17, 9, 7, 4, 2, 11, 16, 12, 3, 5, 26, 14])
