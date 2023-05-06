from functools import cmp_to_key
from lib.linked_list import get_sorted_linked_list


def get_list_length(head):
    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next
    return count


def compare_lists(a, b):
    return get_list_length(a) - get_list_length(b)


def merge(lists):
    sorted_lists = sorted(lists, key=cmp_to_key(compare_lists))
    print(sorted_lists)


merge([
    get_sorted_linked_list(7, prefix='list_1')[0],
    get_sorted_linked_list(5, 3, prefix='list_2')[0],
    get_sorted_linked_list(6, 5, prefix='list_3')[0]
])
