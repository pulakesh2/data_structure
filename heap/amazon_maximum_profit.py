import heapq

# logic
def max_profit(arr):
    # create min heap
    min_heap = []

    # sort the array based on expiry date
    arr.sort(key=lambda x: (x[0], x[1]))

    # time set to 0
    time  = 0

    # check if product is not expired then add to min heap
    for i in range(len(arr)):

        # get expiry date and profit
        expiry = arr[i][0]
        profit = arr[i][1]

        # if product not expired add to the min heap
        if expiry > time:
            time += 1
            heapq.heappush(min_heap, profit)

        # if current profit better than peek of min heap then pop and add new profit to the min heap
        elif profit > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, profit)


    # use ans variable to store the answer
    ans = 0

    # while min heap is not empty add element to the ans variable and return it
    while min_heap:
        ans += heapq.heappop(min_heap)

    return ans


data = [[3,6], [1,5],[3,3],[2,1],[3,9]]

print(max_profit(data))