def problem(arr, target):
    hashset = set()

    total = 0

    for item in arr:
        total += item
        hash_target = total - target
        if hash_target in hashset or hash_target == 0:
            return True

        hashset.add(total)

    return False


arr = [2,3,9,-4,1,-6,6,2,5]

print(problem(arr, 6))
