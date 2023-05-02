import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+2)
dp[1] = 0
dp[2] = 2
dp[3] = 3
 
if n > 3:
    for i in range(4, n+1):
        x = dp[i-1] + dp[i-2]
        if x > 10:
            dp[i] = x % 10
        else:
            dp[i] = x
print(dp[n])