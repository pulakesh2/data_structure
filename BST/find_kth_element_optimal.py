from create_BST import root



def problem(root, k):
    # create ans and count variable
    ans = float('inf')
    count = 0

    # logic to check kth element
    def in_order(root, k):
        nonlocal ans
        nonlocal count

        # if root is none return
        if root is None:
            return

        # check if ans is infinite then go for left side
        if ans == float('inf'):
            in_order(root.left, k)

        # when return back update count by 1
        count += 1

        # if match then update ans and return
        if count == k:
            ans = root.value
            return ans

        # check still infinite go for right side
        if ans == float('inf'):
            in_order(root.right, k)

        # return the function
        return

    # call the function it will update ans value
    in_order(root, k)

    return -1 if ans == float('inf') else ans



print(problem(root, 37))
