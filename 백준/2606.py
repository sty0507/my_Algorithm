from collections import deque
import sys

input = sys.stdin.readline
n = int(input()) # 컴퓨터 수
k = int(input()) # 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(n+1)]

visited = [False] * (k+10)
for i in range(k):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def bfs(start, graph, visited):
    cnt = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt-1
print(bfs(1, graph, visited))
