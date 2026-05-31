import math
from functools import cmp_to_key

# use comparator operator
def comaprator(a,b):

    # find factors of both numbers
    fact_a = factors(a)
    fact_b = factors(b)

    # use for ascending order
    if fact_a < fact_b:
        return -1
    elif fact_a > fact_b:
        return 1

    # if both factors same, compare the magnitude
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

# main problem
def problem(arr):

    # use comparator operator in python
    arr.sort(key = cmp_to_key(comaprator))
    return arr


# find out no of factors
def factors(num):

    # get the iteration
    iteration = int(math.sqrt(num))

    # var to store no of factors
    count = 0

    # count factors
    for i in range(1, iteration + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2

    return count



print(problem(arr = [9,3,10,6,4]))