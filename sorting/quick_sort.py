from quick import quick

# use quick sort
def quick_sort(arr, start, end):
    if start >= end:
        return

    # return the pivot index
    pi = quick(arr, start, end)
    quick_sort(arr, start, pi - 1)
    quick_sort(arr, pi + 1, end)

arr = [54,26,20,17,44,31,55,74,93]

print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)