from lxml.objectify import NoneElement

from linked_list import h1, h2

def merge(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if h1.val <= h2.val:
        head = h1
        h1 = h1.next

    else:
        head = h2
        h2 = h2.next

    temp = head

    while h1 is not None and h2 is not None:
        if h1.val <= h2.val:
            temp.next = h1
            h1 = h1.next
        else:
            temp.next = h2
            h2 = h2.next

        temp = temp.next

    if h1 is not None:
        temp.next = h1
    else:
        temp.next = h2

    return head


