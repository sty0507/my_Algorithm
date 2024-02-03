# math를 사용해서 푼 코드
import math
def solution(n):
    if math.sqrt(n).is_integer():
        return math.pow(math.sqrt(n)+1, 2)
    else:
        return -1
    
# math 안사용해서 푼 코드
def solution(n):
    num = n ** (1/2) # 1/2 제곱
    if num % 1 == 0: # 정수인지 판별, 이렇게 하면 소수점 뒷부분이 나옴
        return (num+1) ** 2
    else:
        return -1