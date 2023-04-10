import sys
input = sys.stdin.readline
t = int(input())
dp = []
dp.append(1)
dp.append(2)
dp.append(4)
dp.append(7)
for k in range(t):
    n = int(input())
    for i in range(len(dp), n+1):
        dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)
    print(dp[n-1])