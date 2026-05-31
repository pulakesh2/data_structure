# create the class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# create the node
node1 = Node(3)
node2 = Node(3)
node3 = Node(3)
node4 = Node(3)
node5 = Node(3)

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


def delete_duplicates(head, val):

    if head.val == val:
        while head and head == val:
            head = head.next

    if head is None:
        return None

    temp = head

    while temp is not None and temp.next is not None:
        if temp.next.val == val:
            curr = temp.next
            while curr.next.val == val:
                curr = curr.next
                if curr.next is None:
                    break

            temp.next = curr.next

        temp = temp.next

    return head




print('befor deleting the elements')
linked_list(node1)

print('after deleting the elements')
head = delete_duplicates(node1, 3)
linked_list(head)