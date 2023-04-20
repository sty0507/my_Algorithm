import sys
sys.setrecursionlimit(10**7) # 재귀 제한 허용치 늘려줌
input = sys.stdin.readline
n = int(input())
# graph = [[] for _ in range(n+1)]
graph = []
result = []
count = 0

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

nx = [0,0,-1,1]
ny = [-1,1,0,0]

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            dfs(dx, dy)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(count)
            count = 0

result.sort()

print(len(result))
for i in result:
    print(i)