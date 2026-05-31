import heapq

# logic to implement the code
def find_kth_largest_element(arr, k):

    # create the result variable to store the answer
    result = []

    # create the min heap
    min_heap = []

    # looping through k times and assign -1 to result variable, if i is k - 1 then add the current value
    for i in range(k):

        # push to min heap
        heapq.heappush(min_heap, arr[i])

        # add curr element
        if i == k - 1:
            result.append(arr[i])

        # if not add -1
        else:
            result.append(-1)


    # looping start from k to n, if current element is bigger than peek element of min heap than pop peek and push current element
    for i in range(k, len(arr)):

        # check condition
        if arr[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, arr[i])

        # store peek element to the result array
        result.append(min_heap[0])

    # return the result
    return result




arr = [10,18,7,5,16,19,3]
print(find_kth_largest_element(arr, 3))