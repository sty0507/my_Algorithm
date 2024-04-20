from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0 and maps[n-2][m-2] == 0:
        return -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    def bfs(x, y):
        queue = deque()
        queue.append((x,y))
        while queue:
            x , y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        return maps[n-1][m-1]
    answer = bfs(0,0)
    if answer > 1:
        return answer
    else:
        return -1
    

"""
bfs 문제이다. 그냥 상 하 좌 우를 돌가면서 탐색을 해서 현재까지 온 개수로 바꾸는 식, 5번째로 온 칸이면 그 값을 5로 해서 결국은 (n,m)의 위치에는 최종 값이 들어있다.
처음에 -1이 나올 수 있는 경우의 수가 그냥 단순히 (n,m)이 모두 막혀 있을때만 안되는 경우의 수만 생각했는데 테케 중에 오는 길에 막혀 있는 것도 생각을 해야 풀어지는 경우의 수가 있어서 마지막 조건문을 추가했다.
"""