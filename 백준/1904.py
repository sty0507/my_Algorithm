import sys
n = int(sys.stdin.readline())

dp = [0] * (n+5)
dp[0] = 1
dp[1] = 2

if n > 2:
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n-1])