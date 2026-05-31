from create_BST_1 import root


def height(root):
    if root is None:
        return -1

    lh = height(root.left)
    rh = height(root.right)

    return max(lh, rh) + 1

print(height(root))