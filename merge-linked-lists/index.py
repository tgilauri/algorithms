from functools import cmp_to_key
from lib.linked_list import get_sorted_linked_list


def sort(a, b):
    return a.val - b.val


def merge_linked_lists(head_a, head_b):
    cur_a, cur_b = [head_a, head_b] if head_a.val <= head_b.val else [head_b, head_a]
    head = cur_a

    while cur_a.next or cur_b.next:
        if cur_a.next is None:
            cur_a.next = cur_b
            break
        if cur_b.next is None:
            cur_b.next = cur_a
            break
        if cur_a.val <= cur_b.val <= cur_a.next.val:
            tmp_cur_a_next = cur_a.next
            tmp_cur_b_next = cur_b.next

            cur_a.next = cur_b
            cur_a = cur_b
            cur_a.next = tmp_cur_a_next
            cur_b = tmp_cur_b_next
        else:
            cur_a = cur_a.next
    return head


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
linked_list_second = get_sorted_linked_list(4, 3)
linked_list_third = get_sorted_linked_list(5)

# head_sorted = merge_linked_lists(linked_list[0], linked_list_second[0])

head_sorted = merge_linked_lists(get_sorted_linked_list(amount=5, prefix='list_1')[0],
                                 get_sorted_linked_list(amount=5, prefix='list_2')[0])

print(head_sorted)
