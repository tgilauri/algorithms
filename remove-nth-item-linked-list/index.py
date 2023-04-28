from lib.linked_list import get_sorted_linked_list


def remove_item_from_end(head, nth):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    iteration = 0

    while True:
        slow = slow.next
        if iteration == 0:
            tmp = fast
            for i in range(nth + 2):
                tmp = tmp.next
            fast = tmp
            iteration += 1
        else:
            fast = fast.next
        if fast is None:
            slow.next = slow.next.next
            break
    return head


linked_list = get_sorted_linked_list(10)
remove_item_from_end(linked_list[0], 3)
