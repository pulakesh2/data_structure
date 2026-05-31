from collections import deque

def nearest_el_on_left(arr):

    result = [-1]

    stack = deque()
    stack.append(0)

    for i in range(1, len(arr)):
        if arr[stack[-1]] < arr[i]:
            result.append(stack[-1])

        else:
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                stack.pop()

            if len(stack) > 0:
                result.append(stack[-1])
            else:
                result.append(i)

        stack.append(i)


    return result


arr1 = [8,2,4,9,7,5,3,10]
print(nearest_el_on_left(arr1))