import heapq
from heapq import heappop, heappush


def merge_lists(lists):
    heap = [x for x in lists]
    heapq.heapify(heap)
    head = last = None

    while heap:
        min = heappop(heap)
        if head is None:
            head = min
            last = min
        else:
            last.next = min
            last = min

        if min.next:
            heappush(heap, min.next)

    return head
