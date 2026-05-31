def merge(arr, start, end, mid):
    p1 = start
    p2 = mid + 1

    result = []

    while p1 <= mid and p2 <= end:
        if arr[p1] <= arr[p2]:
            result.append(arr[p1])
            p1 += 1
        else:
            result.append(arr[p2])
            p2 += 1

    while p1 <= mid:
        result.append(arr[p1])
        p1 += 1

    while p2 <= end:
        result.append(arr[p2])
        p2 += 1

    for i in range(len(result)):
        arr[i + start] = result[i]

    return arr






