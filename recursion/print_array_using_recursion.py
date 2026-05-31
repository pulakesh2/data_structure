def print_array(arr):
    length = len(arr)
    total = 0
    maxi = float('-inf')

    total, maxi = helper(arr, 0, length, total, maxi)

    return f'maximum value: {maxi} and total value: {total}'

def helper(arr, start, end, total, maxi):
    # base case
    if start == end:
        return total, maxi

    # get the element
    element = arr[start]

    # assign max
    if element > maxi:
        maxi = element

    # print curr element
    print(element)

    # recursion
    return helper(arr, start + 1, end, total + element, maxi)




