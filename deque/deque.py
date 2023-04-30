class Dequeue:
    def __init__(self, size, start_idx=0, extensible=False):
        self.arr = [None] * size
        self.size = size
        self.length = 0
        self.start_idx = start_idx
        self.extensible = extensible

    def __get_new_item_idx(self):
        return (self.start_idx + self.length) % self.size

    def __get_last_item_idx(self):
        return self.start_idx + self.length - 1 if self.start_idx == 0 else self.__get_new_item_idx() - 1

    def push_front(self, item):
        if self.length < self.size:
            new_idx = self.start_idx - 1 if self.start_idx > 0 else self.size - 1
            self.arr[new_idx] = item
            self.start_idx = new_idx
            self.length += 1
            if self.extensible:
                self.extend_if_needed()
        else:
            raise Exception('deque is full')

    def push_back(self, item):
        if self.length < self.size:
            new_idx = self.__get_new_item_idx()
            self.arr[new_idx] = item
            self.length += 1
            if self.extensible:
                self.extend_if_needed()
        else:
            raise Exception('deque is full')

    def pop_front(self):
        if self.is_empty():
            return None
        new_idx = self.start_idx + 1 if self.start_idx < self.size - 1 else 0
        item = self.arr[self.start_idx]
        self.arr[self.start_idx] = None
        self.length -= 1
        self.start_idx = new_idx if self.length > 0 else 0
        return item

    def pop_back(self):
        if self.is_empty():
            return None
        last_item_idx = self.__get_last_item_idx()
        item = self.arr[last_item_idx]
        self.arr[last_item_idx] = None
        self.length -= 1
        self.start_idx = self.start_idx if self.length > 0 else 0
        return item

    def get_front(self):
        return self.arr[self.start_idx]

    def get_back(self):
        return self.arr[self.__get_last_item_idx()]

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.length = 0
        self.start_idx = 0

    def extend_if_needed(self):
        if self.length == self.size:
            if self.start_idx == 0:
                new_arr = self.arr + ([None] * self.size)
            else:
                new_arr = self.arr[self.start_idx:] + self.arr[0:self.start_idx] + [None] * self.size
                self.start_idx = 0
            self.arr = new_arr
            self.size *= 2


deque = Dequeue(5, 2, True)

deque.push_back(1)
deque.push_back(2)
deque.push_back(3)
deque.push_front(4)
deque.push_front(5)
deque.push_front(6)
deque.push_back(7)
deque.push_back(8)
deque.push_back(9)
deque.push_back(10)
deque.push_back(11)
deque.push_front(12)

print(deque.get_back())
print(deque.get_front())


print(deque.arr)