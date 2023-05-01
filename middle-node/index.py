from lib.linked_list import get_sorted_linked_list

def middle_node(head):
    if not head:
        return head

    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    middle = int(len(nodes) / 2)
    print(middle)
    return nodes[middle]


print(middle_node(get_sorted_linked_list(6)[0]).val)