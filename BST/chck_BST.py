from create_BST import root

def check_BST(root, mini, maxi):
    # in leaf node return True
    if root is None:
        return True

    # if value is between min and max return True
    if mini <= root.value <= maxi:

        # check left BST
        l = check_BST(root.left, mini, root.value - 1)
        if not l:
            return False

        # check right BST
        r = check_BST(root.right, root.value + 1, maxi)
        if not r:
            return False

        #
        return True

    else:
        #
        return False

print(check_BST(root, float('-inf'), float('inf')))