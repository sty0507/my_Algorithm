n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# dp = [0] * (n*m)
# dp[0] = arr[n-1][m-1]

# i = n-1 # 세로
# j = m-1 # 가로
# k = 1

# if i == 0 and j == 0:
#     print(arr[0][0])
# else:    
#     while i >= 0 and j >= 0:
#         if i == 0 and j == 0:
#             break
#         if (i-1) >= 0 and (j-1) >= 0:
#             max1 = max(arr[i-1][j-1], arr[i][j-1], arr[i-1][j])
#             if  max1 == arr[i-1][j-1]:
#                 i -= 1
#                 j -= 1
#             elif max1 == arr[i-1][j]:
#                 i -= 1
#             elif max1 == arr[i][j-1]:
#                 j -= 1
#         elif (i-1) >= 0 :
#             i -= 1
#         elif (j-1) >= 0:
#             j -= 1
#         dp[k] = dp[k-1] + arr[i][j]
#         k += 1
#     print(max(dp))
dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
print(dp[n][m])


