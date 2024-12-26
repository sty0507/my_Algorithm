import sys

N = int(sys.stdin.readline())

table = list(map(int, sys.stdin.readline().split()))

max_dp = table
min_dp = table

for _ in range(N - 1):
    table = list(map(int, sys.stdin.readline().split()))
    max_dp = [table[0] + max(max_dp[0], max_dp[1]), table[1] + max(max_dp), table[2] + max(max_dp[1], max_dp[2])]
    min_dp = [table[0] + min(min_dp[0], min_dp[1]), table[1] + min(min_dp), table[2] + min(min_dp[1], min_dp[2])]

print(max(max_dp), min(min_dp))


"""
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]
"""

"""
# dp식 풀이 - 1
dp1 = [0] * N
dp2 = [0] * N
dp3 = [0] * N

dp1[0], dp2[0], dp3[0] = table[0][0], table[0][1], table[0][2]

for i in range(1, N):
    dp1[i] = table[i][0] + max(dp1[i-1], dp2[i-1])
    dp2[i] = table[i][1] + max(dp1[i-1], dp2[i-1], dp3[i-1])
    dp3[i] = table[i][2] + max(dp2[i-1], dp3[i-1])

print(max(dp3))
"""

"""
#dp 식 풀이 - 2

dp = [[0] * (N) for _ in range(N)]
dp[0] = table[0]
max_result = 0

for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = max(table[i][j] + dp[i-1][j], table[i][j] + dp[i-1][j+1])
        elif j == N-1:
            dp[i][j] = max(table[i][j] + dp[i-1][j], table[i][j] + dp[i-1][j-1])
        else:
            dp[i][j] = max(table[i][j] + dp[i-1][j-1], table[i][j] + dp[i-1][j+1], table[i][j] + dp[i-1][j])

print(max(dp[N-1]), end=" ")

dp = [[0] * (N) for _ in range(N)]
dp[0] = table[0]

for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = min(table[i][j] + dp[i-1][j], table[i][j] + dp[i-1][j+1])
        elif j == N-1:
            dp[i][j] = min(table[i][j] + dp[i-1][j], table[i][j] + dp[i-1][j-1])
        else:
            dp[i][j] = min(table[i][j] + dp[i-1][j-1], table[i][j] + dp[i-1][j+1], table[i][j] + dp[i-1][j])

print(min(dp[N-1]))
"""
