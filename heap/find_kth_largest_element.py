import heapq


# using max_heap
def find_kth_largest_element(arr, k):

    # create max_heap
    max_heap = []

    # push all the element to the max heap
    for item in arr:
        heapq.heappush(max_heap, -item)

    # pop k - 1 element
    for _ in range(k - 1):
        heapq.heappop(max_heap)

    # store kth element in the variable and return it
    kth_element = heapq.heappop(max_heap)

    return -kth_element




# use sorting
def find_kth_largest_element_using_sorting(arr, k):
    arr.sort(reverse=True)

    return arr[k - 1]



# use min heap
def find_kth_largest_element_using_min_heap(arr, k):
    # create min heap
    min_heap = []

    # store k number element to the min heap
    for i in range(k):
        heapq.heappush(min_heap, arr[i])

    # now check if current element greater than peek element of min heap
    for i in range(k, len(arr)):

        # if yes than pop it and push current element
        if arr[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, arr[i])

    # return peek element of min heap
    return min_heap[0]

arr = [8,5,1,2,4,9,7]

print(find_kth_largest_element_using_min_heap(arr, 3))