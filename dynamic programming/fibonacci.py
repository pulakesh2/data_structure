def print_fibonacci(n):
    # create dp
    dp = [-1] * (n + 1)

    # create fibonacci function
    def fibonacci(n):
        # use dp locally
        nonlocal dp

        # if n is less than 1 add n to n index
        if n <= 1:
            dp[n] = n
            return dp[n]

        # if already present then return the dp[n] value
        if dp[n] != -1:
            return dp[n]

        # find value fibonacci n - 1 and n -2
        ans = fibonacci(n - 1) + fibonacci(n - 2)
        dp[n] = ans
        return dp[n]

    fibonacci(n)

    return dp[-1]


print(print_fibonacci(6))