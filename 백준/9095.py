dp = [0,1,2,4]
def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return dp[n - 3] + dp[n - 2] + dp[n - 1]

for i in range(4, 15):
    dp.append(0)
t = int(input())
for i in range(0, t):
    n = int(input())
    for j in range(0, n+1):
        dp[j] = sol(j)
    print("%d"%dp[j])
