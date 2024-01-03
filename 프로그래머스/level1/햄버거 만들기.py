# 시간이 오래 걸리지만 통과한 내 코드
def solution(ingredient):
    front = []
    answer = 0
    for i in ingredient:
        front.append(i)
        if len(front) >= 4:
            if front[-1] == 1 and front[-2] == 3 and front[-3] == 2 and front[-4] == 1:
                front.pop()
                front.pop()
                front.pop()
                front.pop()
                answer += 1
    return answer

# 다른 사람 코드
# 나랑 같은 원리이지만 좀 더 쉽고 간결하게 코드를 작성함
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt
