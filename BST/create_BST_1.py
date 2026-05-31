class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create nodes
root = Node(5)
node1 = Node(8)
node2 = Node(8)
node3 = Node(8)
node4 = Node(5)
node5 = Node(3)
node6 = Node(6)
node7 = Node(-10)
node8 = Node(1)

# joining branches
root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node6.left = node7
node6.right = node8

