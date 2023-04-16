import sys

n = int(input())

dp = [0] * (n+1)

dp[0] = 3
dp[1] = 7

if n > 2:
    for i in range(2, n+1):
        dp[i] = (dp[i-2] + (2 * dp[i-1])) % 9901

print(dp[n-1])