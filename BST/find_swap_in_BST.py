from create_BST import root

def find_swap(root):
    prev = None
    first = second = None

    def recover(root):
        nonlocal first, second, prev

        if root is None:
            return

        recover(root.left)

        if prev is not None and prev.value > root.value and first is None:
            first = prev
            second = root

        elif prev is not None and prev.value > root.value:
            second = root

        prev = root

        recover(root.right)

    recover(root)

    return first.value, second.value

find_swap(root)