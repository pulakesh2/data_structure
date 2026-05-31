from collections import deque


def vaild_parenthesis(s):
    # create the stack
    stack = deque()

    # loop through each letter
    for char in s:

        # if opening then push to the stack
        if char == '(' or char == '[' or char == '{':
            stack.append(char)

        # if closing then check the top element if open then pop else return False
        elif char == ')':
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False

        elif char == ']':
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False

        elif char == '}':
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False

    # if stack is empty then return True else False
    return True if len(stack) == 0 else False


print(vaild_parenthesis("({()})"))