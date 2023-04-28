# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_num_from_list(node):
    num = ''
    cur = node
    while (True):
        num = str(cur.val) + num
        if cur.next is None:
            break
        cur = cur.next
    return int(num)


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    int_first = get_num_from_list(node=l1)
    int_sec = get_num_from_list(node=l2)

    result = str(int_first + int_sec)
    result_nodes_list = []

    for i in range(len(result), 0, -1):
        node = ListNode(val=int(result[i]), next=None)
        result_nodes_list.append(node)
        if i > 0:
            result_nodes_list[i - 1].next = node
    return result_nodes_list[0]

print(addTwoNumbers())