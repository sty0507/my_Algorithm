import sys
sys.setrecursionlimit(10**7) # 재귀 제한 허용치 늘려줌
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] == True
            dfs(i)

cnt = 0

for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)
print(cnt)