class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
tail = Node(50)

head.next = node1
node1.prev = None

node1.next = node2
node1.prev = head

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = tail

tail.prev = node3
tail.next = None


