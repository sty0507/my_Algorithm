import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def dfs(start):
    for i in graph[start]:
            if visited[i] == 0:
                visited[i] = start
                dfs(i)
dfs(1)

for v in visited[2:]:
     print(v)

"""
input:
7
1 6
6 3
3 5
4 1
2 4
4 7

graph:
[[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
"""