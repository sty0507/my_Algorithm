import sys

n = int(sys.stdin.readline())
wine = [0] * 10001
dp = [0] * 10001
for i in range(n):
    wine[i] = int(sys.stdin.readline())

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    for i in range(2, n+1):
        dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])
    print(dp[n])