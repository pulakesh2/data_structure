def problem(arr):
    first = -1
    second = -1

    for i in range(1, len(arr)):
        curr = arr[i]
        prev = arr[i - 1]

        if prev > curr:
            if first == -1:
                first = prev
                second = curr
            else:
                second = curr


    return first, second


print(problem(arr = [2,6,10,23,19,20,14]))