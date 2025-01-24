import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(0, N):
        if arr[i] in s:
            continue
        s.append(arr[i])
        dfs(arr[i])
        s.pop()

s = []

dfs(0)