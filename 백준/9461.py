import sys

t = int(sys.stdin.readline()) # 시간 초과 안남, input() 보다
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1
for i in range(0, t):
    n = int(sys.stdin.readline())
    for j in range(3, n):
        dp[j] = dp[j-2] + dp[j-3]
    print(dp[n-1])

