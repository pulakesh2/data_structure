class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None # only for level order

# create nodes
root = Node(15)
node1 = Node(10)
node2 = Node(21)
node3 = Node(5)
node4 = Node(27)
node5 = Node(1)
node6 = Node(8)
node7 = Node(24)
node8 = Node(34)

# joining branches
root.left = node1
root.right = node2

node1.left = node3

node2.right = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8
