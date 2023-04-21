import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
field = []

for i in range(n):
    field.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
def dfs(x, y):
    if x >= n or y >= n:
        return False
    
    value = field[x][y]
    if value == -1:
        print("HaruHaru")
        exit(0)
    
    
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x + value, y)
        dfs(x, y + value)
dfs(0 ,0)
print("Hing")