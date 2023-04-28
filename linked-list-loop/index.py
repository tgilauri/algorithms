from lib.linked_list import get_sorted_linked_list

def has_loop(head):
    if head is None:
        return head

    slow = head
    fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


sorted_linked_list = get_sorted_linked_list(5)
tail = sorted_linked_list[-1]
tail.next = sorted_linked_list[3]
print(has_loop(sorted_linked_list[0]))
