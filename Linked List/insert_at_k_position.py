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

# size
def linked_list(node):
    temp = node
    size = 0

    while temp is not None:
        print(temp.val)
        temp = temp.next
        size += 1

    # return size


# insert at k position
def insert_at_k(head, k, val):
    temp = head
    position = 1

    if k == 1:
        new_node = Node(val)
        new_node.next = head
        return new_node

    while position < k - 1:
        position += 1
        temp = temp.next

    new_node = Node(val)
    curr_node = temp.next
    temp.next = new_node
    new_node.next = curr_node

    return head



head = insert_at_k(node1, 1, 3)

print(linked_list(head))



