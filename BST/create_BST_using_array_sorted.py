from create_BST import Node
from order import in_order

def problem(arr, start, end):
    # if exceed then return None
    if start > end:
        return None
    # create Node
    else:
        # find middle element
        mid = (start + end) // 2

        # create node
        nn = Node(arr[mid])

        # join nodes
        nn.left = problem(arr, start, mid - 1)
        nn.right = problem(arr, mid + 1, end)

        # return node
        return nn

arr = [5, 10, 15, 20, 25, 30]

root = problem(arr, 0, len(arr)-1)
in_order(root)