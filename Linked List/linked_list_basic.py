# create the class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# create the node
node1 = Node(1)
node2 = Node(2)
node3 = Node(   3)
node4 = Node(4)
node5 = Node(5)

# link the node
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5



def linked_list(node):
    temp = node
    size = 0

    while temp is not None:
        print(temp.val)
        temp = temp.next
        size += 1

    return size


print(f'size of the link list: {linked_list(node1)}')

