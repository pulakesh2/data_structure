from create_BST import root

class Pair:
    def __init__(self, ht, dia):
        self.ht = ht
        self.dia = dia


def find_distance(root):

    # if root is None return (-1, 0) pair
    if root is None:
        np = Pair(-1, 0)
        return np

    # check left pair and right pair
    left_pair = find_distance(root.left)
    right_pair = find_distance(root.right)

    # create a pair
    new_pair = Pair(-1,0)

    # its height is max of left or right plus 1
    new_pair.ht = max(left_pair.ht, right_pair.ht) + 1

    # create a dia for current node
    dia_new = left_pair.ht + right_pair.ht + 2

    # assign dia which is max of new dia and max of left or right dia
    new_pair.dia = max(max(left_pair.dia, right_pair.dia), dia_new)

    # return new_pair
    return new_pair

def problem(root):

    # store the pair in ans and return the dia
    ans = find_distance(root)
    return ans.dia


print(problem(root))