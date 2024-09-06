from collections import deque
import sys

input = sys.stdin.readline # sys.stdin.readline을 사용하도록 간단하게 만들어주는 작업
n = int(input()) # 컴퓨터 수
k = int(input()) # 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(n+1)] # graph 변수 2차원 리스트로 초기화

visited = [False] * (k+10) # visited 변수 False로 초기화
for i in range(k): # k번씩 돌면서 입력을 받음
    # a,b를 각각 받아 서로의 인덱스에 서로를 더해준다.
    # 입력이 1, 2일때는 1번 인덱스에 2를, 2번 인덱스에 1를 넣어준다.
    # 이 뜻은 1번 인덱스에 있는 값들과 연결되어 있다고 볼 수 있다.
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def bfs(start, graph, visited):
    cnt = 0
    # 큐의 시작을 [start]로 여기서는 1이다.
    # 1부터 탐색을 하겠다는 뜻이다.
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

# bfs를 통해 탐색을 통해 1번과 연결되어 있는 노드의 개수를 count해서 return한다.
print(bfs(1, graph, visited))