import sys
n = int(sys.stdin.readline())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == (n-1) and j == (n-1):
            print(dp[i][j])
            break
        cnt = arr[i][j]
        if j + cnt < n:
            dp[i][j+cnt] += dp[i][j]
        if i + cnt < n:
            dp[i+cnt][j] += dp[i][j]
        