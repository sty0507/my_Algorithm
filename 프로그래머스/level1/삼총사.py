# 내가 짠 코드
def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

# 다른 사람 풀이
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt

"""
나는 무지성으로 3중 반복문을 사용했다.
조합으로 어떻게 하면 될 거 같았지만 모듈도 모르고 머리가 잘 안돌아가서 무지성 3중 반복문을 사용했다.

그런데 파이썬에는 itertools에서 지원하는 combinations라는 조합 관련된 함수가 있다.
첫번째 인자의 리스트 값에서 무작위로 뒤에 인자 값 만큼 뽑아서 값을 넘기고, 그 값을 sum 함수를 통해서 0인지 비교를 한다.
파이썬의 코테에 유리한 함수를 좀 찾아서 공부를 해보자
"""