def power(x , n):
    if n == 0:
        return 1

    return x * power(x, n - 1)

print(power(4, 5))

# optimal solution
def power_optimal(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        y = power_optimal(x, n // 2)
        return y * y
    else:
        y = power_optimal(x, (n - 1) // 2)
        return x * y * y

print(power_optimal(4, 5))