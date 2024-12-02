import sys
from collections import deque

n, m, v = map(int, (sys.stdin.readline().split()))

#n, m, v = 4, 5, 1

node = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
results = []
"""
4 5 1
1 2 
1 3
1 4
2 4
3 4

-> 
node = [
    [2, 3, 4],
    [1, 4],
    [1, 4],
    [1, 2, 3]
]
"""

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    node[x][y] = node[y][x] = 1

def dfs(node, i, visited):
    stack = [i]
    while stack:
        value = stack.pop()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True

        for v in range(len(node[value])-1, -1, -1):
            if (node[value][v] == 1) and (not visited[v]):
                stack.append(v)
def bfs(node, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
            for v in range(len(node[value])):
                if node[value][v] == 1 and not visited[v]:
                    queue.append(v)

dfs(node, v, visited)
visited = [False] * (n+1)
print()
bfs(node, v, visited)

