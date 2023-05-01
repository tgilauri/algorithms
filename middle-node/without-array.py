from lib.linked_list import get_sorted_linked_list


def middle_node(head):
    if not head:
        return head

    counter = 0
    cur = head
    while cur:
        counter += 1
        cur = cur.next

    middle = int(counter / 2)
    print(middle)

    cur = head
    for i in range(1, middle + 1):
        cur = cur.next
    return cur


print(middle_node(get_sorted_linked_list(6)[0]).val)
