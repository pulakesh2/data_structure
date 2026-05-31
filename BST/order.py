from create_BST import root

# in order of the BST
def in_order(root):
    if root is None:
        return

    in_order(root.left)
    print(root.value)
    in_order(root.right)

# pre order of the BST
def pre_order(root):
    if root is None:
        return

    print(root.value)
    in_order(root.left)
    in_order(root.right)


# post order of the BST
def post_order(root):
    if root is None:
        return

    in_order(root.left)
    in_order(root.right)
    print(root.value)


