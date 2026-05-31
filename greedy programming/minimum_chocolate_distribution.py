# create main function
def problem(arr):

    # create right arr and left arr
    right_arr = right_side_check(arr)
    left_arr = left_side_check(arr)

    # create ans variable to store answer
    ans = 0


    # which has max we add to the answer
    for i in range(len(arr)):
        ans += max(right_arr[i], left_arr[i])

    # return the ans
    return ans

# check if current element greater than left element
def right_side_check(arr):
    result_right = [1]

    # loop through the array
    for i in range(1, len(arr)):
        # if yes, then add 1 to previous value and add to the result array
        if arr[i] > arr[i-1]:
            result_right.append(result_right[i-1] + 1)

        # if no, then add 1 to the result array
        else:
            result_right.append(1)

    # return the array
    return result_right


# it will check current element less than the next element
def left_side_check(arr):
    result_left = [1] * len(arr)

    # loop the array in reversed
    for i in range(len(arr) - 2, -1, -1):

        # if right element greater than current element add right element value + 1
        if arr[i] > arr[i+1]:
            result_left[i] = result_left[i+1] + 1

        # else add 1 to the result
        else:
            result_left.insert(0,1)

    # return the result
    return result_left


print(problem(arr = [1,6,3,1,10,12,20,5,2]))