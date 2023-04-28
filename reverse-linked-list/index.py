class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    if head.next is None:
        return head
    if not head:
        return None

    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


reverse_list(
    ListNode(val=1,
             next=ListNode(val=2,
                           next=ListNode(val=3,
                                         next=ListNode(val=4,
                                                       next=ListNode(val=5,
                                                                     next=None))))))
