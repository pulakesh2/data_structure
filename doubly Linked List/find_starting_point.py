from is_cyclic import is_cyclic

def problem(head):
    has_cycle,fast = is_cyclic(head)

    if has_cycle:
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

    else:
        return None
