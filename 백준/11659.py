import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
arr = [0] * (n+1)
for i in range(n):
    arr[i+1] = l[i] + arr[i]
for _ in range(m):
    result = 0
    i, j = map(int, sys.stdin.readline().split())
    if i == j:
        print(l[j-1])
    else:
        print(arr[j] - arr[i-1])