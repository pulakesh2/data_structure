from create_BST import root

def problem(root):
    # create variable to store vertical element
    result = {}
    level = 0

    # fucntion which store element into result array vertically
    def vertical_traversal(root, level):
        nonlocal result

        # if none then return back
        if root is None:
            return

        # check left
        vertical_traversal(root.left, level - 1)

        # create the list in the result dict
        if level not in result:
            result[level] = []

        # add to the result
        result[level].append(root.value)

        # go for the right
        vertical_traversal(root.right, level + 1)

    # print the element vertically using result array
    def print_vertical_order(dictionary):

        # check each index array
        for key in sorted(dictionary.keys()):

            # print each array of each index
            for val in dictionary[key]:
                print(val, end=" ")

    # call the vertical traversal function
    vertical_traversal(root, level)

    # print the element vertically
    print_vertical_order(result)


# run the function
problem(root)