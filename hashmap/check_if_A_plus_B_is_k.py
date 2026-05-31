
def problem(arr, target):
    hash_set = set()

    for item in arr:
        hash_target = target - item
        if hash_target in hash_set:
            return True

        if item not in hash_set:
            hash_set.add(item)

    return False

arr = [8,9,1,-2,4,5,11,-6,4]
k = 11

print(problem(arr, k))