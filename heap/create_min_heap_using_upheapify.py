from up_heapify import upheapify

def create_min_heap(arr):
    for i in range(len(arr) - 1, 0, -1):
        upheapify(arr, i)

    return arr


arr = [7,6,5,4,3,1,2]
print(arr)
print(create_min_heap(arr))