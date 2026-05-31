from functools import cmp_to_key

# create comparator operator
def comparator(a, b):
    # convert to string
    num1 = str(a)
    num2 = str(b)

    # check which string is bigger
    if (num1 + num2) > (num2 + num1):
        return -1
    elif (num1 + num2) < (num2 + num1):
        return 1
    else:
        return 0



def problem(arr):
    # sort based on comparator operator
    arr.sort(key=cmp_to_key(comparator))

    # convert to string
    for i in range(len(arr)):
        arr[i] = str(arr[i])

    # return the string as output
    return "".join(arr)


# arr = [3,30,34,5,9]

print(problem(arr = [10,5,2,8,200]))