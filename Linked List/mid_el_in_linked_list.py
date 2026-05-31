from create_linked_list import node1

def mid_element(head):
    fast = head
    slow = head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow

# print(mid_element(node1))