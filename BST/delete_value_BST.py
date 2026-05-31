from create_BST import root, Node
from min_number_BST import max_element
from order import in_order

def delete(root, value):
    if root is None:
        return root
    elif value > root.value:
        root.right = delete(root.right, value)
    elif value < root.value:
        root.left = delete(root.left, value)
    else:
        if root.right is None and root.left is None:
            return None
        elif root.left is not None and root.right is None:
            return root.left
        elif root.left is None and root.right is not None:
            return root.right
        else:
            maxi = max_element(root.left)
            root.value = maxi
            root.left = delete(root.left, maxi)


    return root

delete(root, 27)
in_order(root)

