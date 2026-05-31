def problem(root):
    # create var to deal with ans
    ans = False

    # sum of the tree
    sum_tree = sum_bst(root)

    # IF odd then return false
    if sum_tree % 2 != 0:
        return False
    
    # check equal partition or not
    sub_sum(root, sum_tree // 2, ans)

    return ans


# sum of bst
def sum_bst(root):
    # if leaf node return 0
    if root is None:
        return 0

    # find left and right sum
    l_sum = sum_bst(root.left)
    r_sum = sum_bst(root.right)

    # return left, right and node value sum
    return l_sum + r_sum + root.value

# check equal partition
def sub_sum(root, h_sum, ans):
    # if leaf node then return 0
    if root is None:
        return 0

    # find left and right sum
    l_sum = sub_sum(root.left, h_sum, ans)
    r_sum = sub_sum(root.right, h_sum, ans)

    # left sum is half or right sum is half then ans become true
    if l_sum == h_sum or r_sum == h_sum:
        ans = True

    return l_sum + r_sum + root.value

