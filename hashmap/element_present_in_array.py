def problem(arr, query):
    # create hashset
    hashset = set()

    # add all element to the hash set ( order of N )
    for element in arr:
        hashset.add(element)

    # create variable to store the answer
    result = []

    # for each query check in the hashset if exist add True else add False
    for el in query:
        result.append(True) if el in hashset else result.append(False)

    return result

print(problem(arr = [10,20,3, 4, 7, 8], query = [7,9,13]))





