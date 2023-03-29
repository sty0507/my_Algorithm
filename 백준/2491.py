import sys
n = int(sys.stdin.readline())
arr = list(map(int, input().split()))

dp1 = [1] * n # 증가수열
dp2 = [1] * n # 감소수열

for i in range(n-1):
    if arr[i] >= arr[i+1]:
        dp1[i+1] += dp1[i]
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        dp2[i+1] += dp2[i]

max1 = max(dp1)
max2 = max(dp2)
print(max(max1, max2))
