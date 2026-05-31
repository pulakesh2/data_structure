# find the unique elements
def problem(arr):
    frequency = set()

    for item in arr:
        frequency.add(item)

    return frequency

arr = [1,1,13,4,5,6,6,7]

print(problem(arr))