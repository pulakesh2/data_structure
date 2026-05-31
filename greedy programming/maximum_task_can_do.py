
# function to get max task
def max_task(arr):

    # assign first task to the count
    count = 1

    # logic to check count
    for i in range(1, len(arr)):
        # if current start time task is bigger than previous end time task then assign
        if arr[i][0] > arr[i - 1][1]:
            count = count + 1

        # else do nothing
        else:
            pass

    return count


tasks = [[1,2],[5,10],[8,10],[7,11],[12,20],[13,19]]

print(max_task(tasks))