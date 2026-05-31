def downheapify(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

    rem = arr.pop()

    down_heapify(arr, 0)

    return ans

def down_heapify(arr, i):

    while 2 * i + 1 < len(arr):
        # find the minimum element
        x = min(arr[2 * i + 1], arr[2 * i + 2], arr[i])

        # if get current element return nothing
        if arr[i] == x:
            return

        # if left side is smallest then swap with the left side
        if x == arr[2 * i + 1]:
            arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
            i = 2 * i + 1

        # if right side is smallest then swap with the right side
        elif x == arr[2 * i + 2]:
            arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
            i = 2 * i + 2


arr = [2,4,5,11,6,7,8,20,12]

print(problem(arr))