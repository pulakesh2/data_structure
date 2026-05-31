from create_BST_1 import root
ans = False

def problem(root, k):
    global ans
    path_sum(root, k)
    return ans

def path_sum(root, k):
    global ans

    if root is None:
        if k == 0:
            ans = True
        return

    path_sum(root.left, k - root.value)
    path_sum(root.right, k - root.value)

print(problem(root, 16))