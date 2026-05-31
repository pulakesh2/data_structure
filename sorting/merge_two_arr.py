def merge(arr1, arr2):
    # use two pointer
    p1 = 0
    p2 = 0

    # find the length of two array
    n = len(arr1)
    m = len(arr2)

    result = []

    # CHECK CONDITION AND APPEND TO THE RESULT
    while p1 < n and p2 < m:
        if arr1[p1] <= arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1

    while p1 < n:
        result.append(arr1[p1])
        p1 += 1

    while p2 < m:
        result.append(arr2[p2])
        p2 += 1

    return result

arr1 = [1,5,6,9,10,11]
arr2 = [2,4,8]

print(merge(arr1, arr2))

