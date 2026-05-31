def problem(arr, target):
    hashmap = dict()
    pair_sum = 0

    for item in arr:
        hash_target = target - item
        if hash_target in hashmap:
            pair_sum += hashmap[hash_target]

        if item not in hashmap:
            hashmap[item] = 1
        else:
            hashmap[item] += 1

    return pair_sum


arr = [3,5,1,2,1,2]
target = 3

print(problem(arr = [1,3,2,1,2,3,1], target = 3))
