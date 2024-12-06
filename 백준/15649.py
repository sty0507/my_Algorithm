import sys

# 백트래킹 관련 문제
# 백트래킹은 간단하게 안될 것 같으면 과감히 돌아가는? 기법 -> 시간 줄일 수 있다.

# 입력을 받는다.
n , m = map(int, sys.stdin.readline().split())
# 빈 리스트를 선언한다.
s = []

# DFS를 사용한다.
def dfs():
    # 현재 s 리스트가 요구하는 m의 길이와 같다면
    if len(s) == m:
        # s 안의 내용들을 공백을 넣어서 출력
        print(' '.join(map(str, s)))
        # 함수 종료해서 호출했던 곳으로 돌아감
        return
    
    # 쌍을 구해야하니 1에서부터 n+1까지 다 돔
    for i in range(1, n+1):
        # i가 s 리스트 안에 없다면
        if i not in s:
            # s에 i를 추가함
            s.append(i)
            # 다시 함수 호출 -> 재귀적
            dfs()
            # 한번쓴 s는 삭제
            s.pop()
        
dfs()