def problem(str):
    # create a hashset
    hashset = set()

    # assign the pointer as 0
    i = j = 0

    length = 0

    # run the loop until length of string
    while j < len(str):

        # if element already present in the hashset then we remove until element is gone and update i
        while((i < j) and (str[j] in hashset)):
            hashset.pop()
            i += 1

        # add element to the hashset
        hashset.add(str[j])

        # 
        length = max(length, j - i + 1)
        j += 1

    return length



str = 'abcdak'

print(problem(str))
