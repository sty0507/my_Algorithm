n = int(input())
dp = [0] * 100100
sta = [0] * 100100
for i in range(0, n):
    sta[i] = int(input())

if n <= 2:
    print(sum(sta))
else:
    dp[0] = sta[0]
    dp[1] = dp[0] + sta[1]
    for i in range(2, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + sta[i-1]) + sta[i]

    print(dp[n])