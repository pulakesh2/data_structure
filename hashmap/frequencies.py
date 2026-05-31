arr = [1,2,2,3,45,4,3,4,5,3]

def problem(arr):
    frequency = {}
    for item in arr:
        if item not in frequency:
            frequency[item] = 1
        else:
            frequency[item] += 1

    return frequency


print(problem(arr))