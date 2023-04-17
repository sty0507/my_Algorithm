import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = i
    for j in range(1, int(math.sqrt(i))+1): # math.sqrt(i)는 i의 제곱근 반환
            dp[i] = min(dp[i], dp[i-j*j]+1)
    
print(dp[n])
