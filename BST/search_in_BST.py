# from create_BST import root

def search(root,value):
    if root is None:
        return False

    if root.value == value:
        return True
    elif value < root.value:
        return search(root.left,value)
    else:
        return search(root.right,value)


# print(search(root,-1))
