def problem(arr):
    hashmap = dict()

    for item in arr:
        if item not in hashmap:
            hashmap[item] = 1
        else:
            hashmap[item] += 1

    for item in arr:
        if hashmap[item] > 1:
            return item

    return None

arr = [4,2,3,2,3,5]
print(problem(arr))
