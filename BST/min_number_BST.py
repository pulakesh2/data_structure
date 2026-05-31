from create_BST import root

def min_element(root):
    if root.left is None:
        return root.value
    else:
        return min_element(root.left)

def max_element(root):
    if root.right is None:
        return root.value
    else:
        return max_element(root.right)

# print(f'minimum element : {min_element(root)}')
# print(f'maximum element : {max_element(root)}')
