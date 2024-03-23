def solution(brown, yellow):
    xpy = int(brown / 2 + 2)
    xy = brown + yellow
    answer = []
    for i in range(1, xpy):
        if i * (xpy-i) == xy:
            answer.append(max(i, (xpy-i)))
            answer.append(min(i, (xpy-i)))
            return answer
    
"""
수학적으로 접근해서 풀 수 있는 문제이다.
가로 세로 길이를 각각 x,y로 할때 xy = brown + yellow이고 x+y = brown / 2 + 2이다.
그래서 반복문을 통해서 1부터 짝이 되는 수를 구하는 방식으로 풀었다.
반복문을 사용하지 않고 그냥 수식으로도 풀 수 있을거 같긴하다.
"""