class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_sorted_linked_list(amount):
    node = ListNode(val=1, next=None)
    result = [node]

    for i in range(2, amount + 1, 1):
        next_node = ListNode(val=i, next=None)
        node.next = next_node
        node = next_node
        result.append(node)
    return result
