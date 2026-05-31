from print_linked_list import print_linked_list
from doubly_linked_list import tail, Node, head


def insert_at_back(tail, data):
    nn = Node(data)
    prev = tail.prev
    prev.next = nn
    nn.next = tail
    nn.prev = prev
    tail.prev = nn

insert_at_back(tail, 45)

print_linked_list(head)
