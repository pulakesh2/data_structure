
def problem(arr):
    # prefix
    total = 0

    hashmap = dict()

    for item in arr:
        total += item

        if total not in hashmap:
            hashmap[total] = 1
        else:
            return True

    return False

arr = [2,2,1,-3,4,3,1,-2,-3,2]
print(problem(arr))