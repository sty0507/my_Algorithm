from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, r, c, visited, field):
    q = deque([(x, y)])
    visited[x][y] = 1
    cost = int(field[x][y])

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < r and 0 <= ny < c and field[nx][ny] != 'X':
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cost += int(field[nx][ny])
                    q.append((nx, ny))

    return visited, cost   

def solution(maps):
    answer = []
    r, c = len(maps), len(maps[0])
    visited = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited, ans = bfs(i, j, r, c, visited, maps)
                answer.append(ans)

    return sorted(answer) if answer else [-1]

"""
반복문을 돌아가면서 숫자면 bfs 함수를 호출한다.
그리고 상 하 좌 우를 도는 리스트 dx, dy를 순서대로 더해서 큐에 값을 넣고 비교를 한다.
visited라는 리스트로 방문 여부를 확인을 해서 반복문을 통해 반복하는 형식이다.

탐색 문제이다.
"""