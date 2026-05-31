

def insert_in_heap(arr, k):
    # first add the element to the array
    arr.append(k)

    # find its length
    i = len(arr) - 1

    # while i is not 0 run the loop
    while i > 0:

        # get parent index
        parent = (i - 1) // 2

        # check parent is bigger than child or not
        if arr[parent] >= arr[i]:

            # swap the nodes
            swap(arr, parent, i)

            # new i is the parent index
            i = parent
        else:
            break

    # return the updated array
    return arr

# swapping two values of the array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


arr = [2,4,5,11,6,7,8,20,12]

print(insert_in_heap(arr, 3))