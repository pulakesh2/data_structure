from collections import deque

def calculate_postfix(s):
    # use stack
    stack = deque()

    # go through each letter
    for num in s:

        # if operator then pop, calculate then add to the stack
        if num == '+' or num == '-' or num == '*' or num == '/':
            a = int(stack.pop())
            b = int(stack.pop())
            if num == '+':
                stack.append(b + a)
            elif num == '-':
                stack.append(b - a)
            elif num == '*':
                stack.append(b * a)
            else:
                stack.append(b / a)
        # else push to the stack
        else:
            stack.append(num)

    # return the top element
    return stack.pop()


print(calculate_postfix('35+2-25*-'))