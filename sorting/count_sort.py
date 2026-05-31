def count_sort(arr):
    # find the min and max element of the array
    mini = min(arr)
    maxi = max(arr)

    # calculate the size
    size = maxi - mini + 1

    # create array with size and value 0
    new_arr = [0] * size

    # use result val to store sorting array
    result = []

    # loop through the given array and logic to store value to new_array
    for i in range(len(arr)):

        new_arr[arr[i] - mini] += 1

    # store the sorting element to the new array
    for i in range(len(new_arr)):
        if new_arr[i] > 0:
            for _ in range(new_arr[i]):
                result.append(i + mini)

    return result

print(count_sort(arr = [10,13,7,4,23,50]))
