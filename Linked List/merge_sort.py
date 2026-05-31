from create_linked_list import node1
from merge_linked_list import merge
from mid_el_in_linked_list import mid_element



def merge_sort(h1):
    if h1 is None or h1.next is None:
        return h1

    mid_el = mid_element(h1)
    h2 = mid_el.next
    mid_el.next = None

    t1 = merge_sort(h1)
    t2 = merge_sort(h2)

    return merge(t1, t2)

merge_sort(node1)

def print_list(h1):
    while h1 is not None:
        print(h1.val)
        h1 = h1.next


print(print_list(node1))
