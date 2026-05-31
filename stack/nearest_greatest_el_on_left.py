from collections import deque

def problem(arr):
    stack = deque()
    result = []

    for i in range(len(arr)):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(i)

    return result

