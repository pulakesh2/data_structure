class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


h1 = Node(2)
node2 = Node(5)
node3 = Node(9)
node4 = Node(14)
node5 = Node(19)

h1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


h2 = Node(3)
n2 = Node(6)
n3 = Node(10)
n4 = Node(11)
n5 = Node(12)

h2.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


