from create_BST import root

def find_ancestor(root, p, q):
    if root is None:
        return None

    if root.value == p or root.value == q:
        return root

    l = find_ancestor(root.left, p, q)
    r = find_ancestor(root.right, p, q)

    if l is None:
        return r

    elif r is None:
        return l
    else:
        return root


ancester = find_ancestor(root, 24,27)
print(ancester.value)
