
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next

