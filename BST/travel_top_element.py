from collections import deque
from create_BST import root

class Pair:
    def __init__(self, x, y):
        self.value = x
        self.level = y

def top_traversal(root):
    result = {}

    q = deque()
    q.append(Pair(root, 0))

    while len(q) > 0:

        # remove leftmost element
        rem = q.popleft()

        # check is it present in hashmap
        if rem.level not in result:
            result[rem.level] = []

        # check is there any element present or not
        if len(result[rem.level]) == 0:
            result[rem.level].append(rem.value.value)
        else:
            pass

        # if left and right exist then add to the queue
        if rem.value.left is not None:
            q.append(Pair(rem.value.left, rem.level - 1))

        if rem.value.right is not None:
            q.append(Pair(rem.value.right, rem.level + 1))

    # check each index array
    for key in sorted(result.keys()):

        # print each array of each index
        for val in result[key]:
            print(val, end=" ")

top_traversal(root)