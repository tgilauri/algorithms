class Node:
    def __init__(self, val, prev):
        self.val = val
        self.prev = prev


class Deque:

    def __init__(self, size=10, extensible=False):
        self.length = 0
        self.size = size
        self.extensible = extensible
        self.head = None
        self.tail = None

    def push_front(self, value):
        if self.length < self.size:
            self.head = Node(val=value, prev=self.head)
            self.length += 1
            if self.extensible:
                self.extend_if_needed()
        else:
            raise Exception('deque is full')

    def push_back(self, value):
        if self.length < self.size:
            self.tail = Node(val=value, prev=self.tail)
            self.length += 1
            if self.extensible:
                self.extend_if_needed()
        else:
            raise Exception('deque is full')

    def pop_front(self):
        if self.is_empty():
            return None
        item = self.head
        self.head = self.head.prev
        self.length -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            return None
        item = self.tail
        self.tail = self.tail.prev
        self.length -= 1
        return item

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.length = 0
        self.head = None
        self.tail = None

    def extend_if_needed(self):
        if self.length == self.size:
            self.size *= 2

    def get_front(self):
        return self.head

    def get_back(self):
        return self.tail


deque = Deque(5, extensible=True)

deque.push_front(1)
deque.push_front(2)
deque.push_front(3)
deque.push_back(4)
deque.push_back(5)
deque.push_back(6)

print(deque.get_front().val)
print(deque.get_back().val)

print(deque.pop_back().val)
print(deque.get_back().val)


