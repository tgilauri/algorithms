class BinTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BiTree:

    def __init__(self):
        self.head = None

    def add(self, val):
        node = BinTreeNode(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while True:
                if val == curr.val:
                    return curr
                if val < curr.val:
                    if not curr.left:
                        curr.left = node
                        return curr.left
                    else:
                        curr = curr.left
                elif val > curr.val:
                    if not curr.right:
                        curr.right = node
                        return curr.right
                    else:
                        curr = curr.right

    def search(self, val):
        curr = self.head
        counter = 0
        while curr:
            counter += 1
            print(f"operation #{counter}")
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def get_head(self):
        return self.head


def create_bi_tree(values):
    _bi_tree = BiTree()

    for val in values:
        _bi_tree.add(val)

    return _bi_tree


bi_tree = create_bi_tree(
    [35, 28, 9, 4, 36, 8, 2, 32, 38, 41, 46, 49, 43, 7, 6, 16, 14, 24, 5, 11, 10, 15, 17, 31, 23, 12, 22, 25, 19, 13])
search_val = bi_tree.search(13)

print(bi_tree.get_head().val)
print(search_val.val)
print(bi_tree.search(99))


def preorder(node):
    print(node.val)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.val)
    if node.right:
        inorder(node.right)


def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.val)
