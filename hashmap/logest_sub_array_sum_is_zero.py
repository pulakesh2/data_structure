

def prefix_sum(arr):
    ans = []
    ans.append(arr[0])

    for i in range(1, len(arr)):
        ans.append(ans[i - 1]  + arr[i])

    return ans

def problem(arr):
    p_sum = prefix_sum(arr)
    hash_map = dict()
    ans = 0

    for i in range(len(p_sum)):

        if p_sum[i] == 0:
            ans = max(ans, i + 1)

        elif p_sum[i] not in hash_map:
            hash_map[p_sum[i]] = i

        else:
            j = hash_map[p_sum[i]]
            length = i - j + 1
            ans = max(ans, length)


    return ans

arr = [3, 2, -1]
print(problem(arr))