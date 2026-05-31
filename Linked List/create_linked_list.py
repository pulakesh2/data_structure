# create the class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# create the node
node1 = Node(1)
node2 = Node(2)
node3 = Node(5)
node4 = Node(3)
node5 = Node(7)
node6 = Node(9)

# link the node
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
