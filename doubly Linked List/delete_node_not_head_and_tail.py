from doubly_linked_list import head
from print_linked_list import print_linked_list

def delete_node(head, data):
    current = head

    while current.data != data:
        current = current.next

    prev = current.prev
    next_el = current.next

    prev.next = next_el
    next_el.prev = prev

    current.next = None
    current.prev = None

    return head



delete_node(head, 20)
print_linked_list(head)

