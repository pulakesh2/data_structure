class Stack:
    # initialize array and the size
    def __init__(self):
        self.stack = []
        self.size = 0

    # push function
    def push(self,x):
        self.stack.append(x)
        self.size += 1

    # pop function
    def pop(self):
        if self.size <= 0:
            raise IndexError('stack underflow')
        self.size -= 1
        return self.stack.pop()

    # size of the stack
    def sizee(self):
        return self.size

    # return the top element
    def peek(self):
        return self.stack[-1]


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # return 3
print(stack.sizee()) # return 3
stack.pop()
print(stack.peek()) # return 2

