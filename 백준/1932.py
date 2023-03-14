import sys

n = int(sys.stdin.readline())

dp = [[0 for col in range(n)] for row in range(n)]
a = [i for i in range(0, n)]
for i in range(0, n):
    a[i] = list(map(int, input().split()))

k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            a[i][j] = a[i][j] + a[i - 1][j]
        elif i == j:
            a[i][j] = a[i][j] + a[i - 1][j - 1]
        else:
            a[i][j] = max(a[i - 1][j - 1], a[i - 1][j]) + a[i][j]
    k += 1
print(max(a[n - 1]))
        