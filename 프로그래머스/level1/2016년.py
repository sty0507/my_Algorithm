# 내 코드
def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = b
    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            day += 31
        elif i == 2:
            day += 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            day += 30
    return days[(day % 7) - 1]

# 다른 사람 코드
def solution(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]
# 엄청 단순하다
# 나의 모든 과정이 담긴 코드이다. 나의 모든 과정을 리스트로 정리를 해서 훨씬 효율적인 코드 인 것 같다.

# 윤년 문제로 2월이 29일까지 있다는 것이 함정이다.