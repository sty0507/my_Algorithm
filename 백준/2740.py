import sys
input = sys.stdin.readline
a = []
b = []

n,m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
m,k = map(int,input().split())
for i in range(m):
    b.append(list(map(int, input().split())))
result = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += a[i][l] * b[l][j]

for i in result:
    for j in i:
        print(j, end=' ')
    print()
