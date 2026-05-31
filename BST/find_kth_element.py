from create_BST import root
from order import in_order


# store the element in the result variable
result = []

# store element logic
def store_the_value(root):
    global result
    if root is None:
        return

    store_the_value(root.left)
    result.append(root.value)
    store_the_value(root.right)

    return result

# find kth element
def find_kth_element(root, k):
    ans = store_the_value(root)

    return ans[k - 1]

print(find_kth_element(root, 3))
