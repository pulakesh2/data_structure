

def quick(arr, start, end):
    pivot = start
    l = start + 1
    r = end


    while l <= r:
        if arr[l] <= arr[pivot]:
            l += 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1

    arr[pivot], arr[r] = arr[r], arr[pivot]

    return r


# arr = [54,26,93,17,77,31,44,55,20]

# arr = [4,6,4,12,8,34,6]
#
# print(quick(arr, 0, len(arr)-1))
