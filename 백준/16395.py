import sys
input = sys.stdin.readline

n, k = map(int, input().split())

pas = [[0] * n for _ in range(n)]
for i in range(len(pas)):
    for j in range(i+1):
        if j == 0 or j == i:
            pas[i][j] = 1
        else:
            pas[i][j] = pas[i-1][j-1] + pas[i-1][j]

print(pas[n-1][k-1])