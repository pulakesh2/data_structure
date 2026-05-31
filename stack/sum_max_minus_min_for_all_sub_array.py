
from collections import deque
from unittest import result

from scipy.ndimage import maximum


def find_smallest_on_left(arr):
    stack = deque()
    result = []

    for i in range(len(arr)):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(i)

    return result

def find_smallest_on_right(arr):
    stack = deque()
    result = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            result.append(len(arr))
        else:
            result.append(stack[-1])

        stack.append(i)

    reverse_result = list(reversed(result))
    return reverse_result

def find_greatest_on_left(arr):
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



def find_greatest_on_right(arr):
    stack = deque()
    result = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            result.append(len(arr))
        else:
            result.append(stack[-1])

        stack.append(i)

    reverse_result = list(reversed(result))
    return reverse_result




arr1 = [1,8,3,5,4,2,11,7]
arr2 = [2,5,3]
smallest_on_left = find_smallest_on_left(arr2)
smallest_on_right = find_smallest_on_right(arr2)
greatest_on_left = find_greatest_on_left(arr2)
greatest_on_right = find_greatest_on_right(arr2)


def problem(arr, smallest_left, smallest_right, greatest_left, greatest_right):
    sum_result = 0

    for i in range(len(arr)):
        count_j = i - smallest_left[i]
        count_k = smallest_right[i] - i
        minimum_time = count_j * count_k


        count_p = i - greatest_left[i]
        count_q = greatest_right[i] - i
        maximum_time = count_p * count_q

        sum_result += arr[i] * (maximum_time - minimum_time)

    return sum_result

print(problem(arr2, smallest_on_left, smallest_on_right, greatest_on_left, greatest_on_right))

