n = int(input())
dp = [0] * 10000
dp[1] = 1
dp[2] = 2
result = 0
if n == 1:
    result = 1
elif n == 2:
    result = 2
else :
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    result = dp[i]



print("%d"% (result % 10007))
