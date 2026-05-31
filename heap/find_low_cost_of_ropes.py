import heapq

def optimal_cost(arr):

    # create variable to store ans
    ans_sum = 0

    # use min heap
    min_heap = []

    # create the min heap
    heapq.heapify(min_heap)

    # store every element of arr in min heap
    for item in arr:
        heapq.heappush(min_heap, item)

    # while size of min_heap greater than 1 get first and second min el, sum them and add to min heap
    while len(min_heap) > 1:
        first_min = heapq.heappop(min_heap)
        second_min = heapq.heappop(min_heap)

        # calculate total and add to ans sum
        total = first_min + second_min
        ans_sum += total

        # add total to the min heap
        heapq.heappush(min_heap, total)

    return ans_sum

print(optimal_cost(arr = [1,2,3,4]))


