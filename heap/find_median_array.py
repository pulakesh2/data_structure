import heapq
def find_median(arr):
    # create two heap max and min
    max_heap = []
    min_heap = []

    # push first element to the max heap
    heapq.heappush(max_heap, -arr[0])

    # now add all element to the max and min heap
    for i in range(1, len(arr)):

        # if current element small then max peek heap add to max heap else add to min heap
        if arr[i] < -max_heap[0]:
            heapq.heappush(max_heap, -arr[i])
        else:
            heapq.heappush(min_heap, arr[i])

    # find the difference between two heap
    diff = len(max_heap) - len(min_heap)

    # if diff is more than one keep calling balance function
    while abs(len(max_heap) - len(min_heap)) > 1:
        balance(max_heap, min_heap)

    # if max heap length is more than min heap return peek of max heap
    if len(max_heap) > len(min_heap):
        return -max_heap[0]

    # if min heap length is higher than return peek of min heap
    elif len(min_heap) > len(max_heap):
        return min_heap[0]

    # if same than average of max and min peek element
    else:
        return (-max_heap[0] + min_heap[0]) / 2


# balance function
def balance(maxi, mini):
    if len(maxi) > len(mini):
        heapq.heappush(mini, -heapq.heappop(maxi))
    else:
        heapq.heappush(maxi, -heapq.heappop(mini))


print(find_median(arr = [2,4,3,5,7,8]))