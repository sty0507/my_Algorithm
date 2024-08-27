import sys

t = int(sys.stdin.readline())
for _ in range(t):
    fi = int(sys.stdin.readline())
    dp = [[0, 0] for k in range(fi + 2)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, fi + 1):
        dp[i][0] = dp[i - 2][0] + dp[i - 1][0]
        dp[i][1] = dp[i - 2][1] + dp[i - 1][1]

    print(dp[fi][0], dp[fi][1])