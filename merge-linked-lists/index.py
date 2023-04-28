from functools import cmp_to_key
from lib.linked_list import get_sorted_linked_list


def sort(a, b):
    return a.val - b.val


def merge_k_lists(lists):
    items = []
    for head in lists:
        curr = head
        while curr:
            items.append(curr)
            curr = curr.next
    sorted_items = sorted(items, key=cmp_to_key(sort))
    for i in range(len(sorted_items) - 1, -1, -1):
        item = sorted_items[i]
        if i != 0:
            sorted_items[i - 1].next = item
    return sorted_items[0]


linked_list = get_sorted_linked_list(5)
linked_list_second = get_sorted_linked_list(5)
linked_list_third = get_sorted_linked_list(5)

print(merge_k_lists([
    linked_list[0],
    linked_list_second[0],
    linked_list_third[0],
]))
