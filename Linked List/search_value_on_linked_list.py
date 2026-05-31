# create the class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# create the node
node1 = Node(1)
node2 = Node(2)
node3 = Node(13)
node4 = Node(4)
node5 = Node(15)

# link the node
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def search(head, val):
    temp = head

    while temp is not None:
        if temp.val == val:
            return True
        temp = temp.next

    return False

print(search(node1, 15))