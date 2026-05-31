from create_BST import root, Node
from order import in_order

def insert(root, value):
    if root is None:
        nn = Node(value)
        return nn

    if value <= root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

insert(root, 10)
in_order(root)
