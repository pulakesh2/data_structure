def problem(arr, target):
    length = len(arr)
    ans = []
    return helper(arr, ans,0, length, target)

def helper(arr, ans, idx, length, target):
    if idx == length:
        return ans

    if arr[idx] == target:
        ans.append(idx)

    return helper(arr, ans, idx+1, length, target)


arr = [4,5,3,1,5,4,5]
print(problem(arr, 5))