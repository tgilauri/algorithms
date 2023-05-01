class ListNode:
    def __init__(self, val=0, next=None, name=None):
        self.val = val
        self.next = next
        self.name = name

    def __lt__(self, other):
        return self.val > other.val


def get_sorted_linked_list(amount, start_val=1, prefix=''):
    node = ListNode(val=start_val, next=None, name='_'.join([prefix, str(start_val)]))
    result = [node]

    for i in range(start_val + 1, start_val + amount + 1, 1):
        next_node = ListNode(val=i, next=None, name='_'.join([prefix, str(i)]))
        node.next = next_node
        node = next_node
        result.append(node)
    return result
