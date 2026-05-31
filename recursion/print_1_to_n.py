# print in increasing order
def problem_inc(num):
    if num == 0:
        return

    problem_inc(num - 1)
    print(num)

# print in decreasing order
def problem_dec(num):
    if num == 0:
        return

    print(num)
    problem_dec(num - 1)


# output
problem_dec(5)
problem_inc(5)


def problem(a,b):
    if a > b:
        return

    print(a)
    problem(a + 1, b)

a = 4
b = 10
print(f'from {a} to {b}')
problem(a,b)