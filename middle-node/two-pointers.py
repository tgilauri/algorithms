from lib.linked_list import get_sorted_linked_list


def middle_node(head):
    if not head:
        return head
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


print(middle_node(get_sorted_linked_list(6)[0]).val)
