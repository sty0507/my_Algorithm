import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * 1002
dp[0] = arr[0]

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])
        else:
            dp[i] = max(dp[i], arr[i])
print(max(dp))