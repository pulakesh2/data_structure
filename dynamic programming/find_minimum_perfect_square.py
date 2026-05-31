import math

def problem(num):
    dp = [-1] * (num + 1)

    def min_square(num):
        nonlocal dp
        if num == 0:
            dp[num] = 0
            return dp[num]

        if dp[num] != -1:
            return dp[num]

        ans = float('inf')

        for i in range(1, int(math.sqrt(num)) + 1):
            ans = min(ans, min_square(num - i * i))

        dp[num] = ans + 1

        return dp[num]

    min_square(num)

    return dp[-1]

print(problem(6))



