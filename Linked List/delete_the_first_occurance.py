# create the class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# create the node
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(3)
node5 = Node(4)

# link the node
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def linked_list(head):
    temp = head

    while temp:
        print(temp.val)
        temp = temp.next


def delete_the_first_occurance(head, val):
    if head is None:
        return head

    if head.val == val:
        nh = head.next
        head.next = None
        head = nh
        return head

    temp = head

    while temp is not None and temp.next is not None:
        if temp.next.val == val:
            temp.next = temp.next.next
            return head
        temp = temp.next

    return head

print('befor deleting the first occurance')
linked_list(node1)
head = delete_the_first_occurance(node1, 1)
print('after deleting the first occurance')
linked_list(head)

