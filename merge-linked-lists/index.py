from functools import cmp_to_key
from lib.linked_list import get_sorted_linked_list


def sort(a, b):
    return a.val - b.val


def merge_linked_lists(head_a, head_b):
    if head_a is None:
        return head_b
    elif head_b is None:
        return head_a

    cur_a, cur_b = [head_a, head_b] if head_a.val <= head_b.val else [head_b, head_a]
    head = cur_a

    while True:
        if cur_a.next is None:
            cur_a.next = cur_b
            break
        if cur_b is None:
            break
        if cur_b.val <= cur_a.next.val:
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
    list_a = lists[0]
    for i in range(1, len(lists)):
        list_b = lists[i]
        list_a = merge_linked_lists(list_a, list_b)
    return list_a


linked_list = get_sorted_linked_list(5)
linked_list_second = get_sorted_linked_list(4, 3)
linked_list_third = get_sorted_linked_list(5)

# head_sorted = merge_linked_lists(linked_list[0], linked_list_second[0])

head_sorted = merge_k_lists([get_sorted_linked_list(amount=5, prefix='list_1')[0],
                             get_sorted_linked_list(amount=5, prefix='list_2')[0]])

print(head_sorted)
