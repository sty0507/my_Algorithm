import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)  # 재귀 제한 허용치 늘려줌

def dfs(x, y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  land[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  land = []
  count = 0
  for _ in range(h):
    land.append(list(map(int, input().split())))
  for i in range(h):
    for j in range(w):
      if land[i][j] == 1:
        dfs(i, j)
        count += 1
  
  print(count)