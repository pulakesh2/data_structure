from create_BST import root
from collections import deque

def level_order(root):
    if root is None:
        return
    # use queue
    queue = deque()

    # add root element first
    queue.append(root)

    while queue:
        # get the size
        size = len(queue)

        # run the loop for queue size
        for i in range(size):

            # pop the first left element
            rem = queue.popleft()

            # if i is less than size append peek element
            if i < size - 1:
                # here i want to access left element of queue
                rem.next = queue[0]
            # else connect to none
            else:
                rem.next = None

            # if left and right present than add to queue
            if rem.left is not None:
                queue.append(rem.left)
            if rem.right is not None:
                queue.append(rem.right)

level_order(root)