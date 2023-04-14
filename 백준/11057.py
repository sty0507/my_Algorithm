import sys

input = sys.stdin.readline

n = int(input())

dp = [[1 for _ in range(10)]for _ in range(n)]

if n == 1:
    print(sum(dp[0]))
else:
    for i in range(1,n):
        for j in range(1,10):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])

    print(sum(dp[n-1]) % 10007)