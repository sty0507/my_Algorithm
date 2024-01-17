# 내 풀이
def solution(n):
    three = []
    answer = 0
    while n > 0:
        three.append(int(n%3))
        n = int(n / 3)
    three.reverse()
    print(three)
    for idx, data in enumerate(three):
        
        answer += data * (3 ** idx)
    return answer

# 다른 사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
    # int()에서 두번째 인자로 변환할 진수의 값을 주면 가능하다. 그러니 3을 줬기에 3진수로 되는 거다.