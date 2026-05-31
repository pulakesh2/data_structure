
from collections import deque

def problem(str):
    stack = deque()

    for char in str:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = []
    while stack:
        result.insert(0, stack.pop())

    return "".join(result)


# str = 'abbcbbcacx'
str = 'abccbe'

print(problem(str))