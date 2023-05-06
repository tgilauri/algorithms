class BinTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

