class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.size -= 1
            return temp.data

    def peek(self):
        if self.head is None:
            return -1
        else:
            return self.head.data

    def get_size(self):
        return self.size

def print_stack(head):
    temp = head
    if temp is None:
        return -1
    else:
        while temp:
            print(temp.data)
            temp = temp.next

stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)


print_stack(stack.head)

print("Size:", stack.get_size())
print("Top:", stack.peek())

print("Popped:", stack.pop())
print("Size after pop:", stack.get_size())