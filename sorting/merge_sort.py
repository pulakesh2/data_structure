from sub_arr_sorted import merge

def merge_sort(arr, start, end):
    mid = (start + end) // 2

    if start == end:
        return

    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    return merge(arr, start, end, mid)


arr = [10,15,3,8,6,2,17,12,18]

print(merge_sort(arr, 0, len(arr)-1))
