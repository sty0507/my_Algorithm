import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = float(input())
dp = arr

for i in range(1, n):
    dp[i] = max(dp[i], dp[i] * dp[i-1])

print("%0.3f" % (max(dp)))