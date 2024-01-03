# 시간초과가 나는 코드
def getnum(n):
    num = []
    for i in range(1, n+1):
        if(n%i == 0):
            num.append(i)
    return num

def solution(number, limit, power):
    att = []
    for data in range(1, number + 1):
        num = getnum(data)
        n = len(num)
        if n > limit:
            n = power
        att.append(n)
    return sum(att)

# 정답 코드
def solution(number, limit, power):
    result = 0
    for i in range(1, number+1):
        num = 0
        for j in range(1,int(i**0.5) + 1):
            if i%j == 0:
                num += 2
        if i**0.5 % j == 0: # 완전제곱수
            num -= 1
        
        if num > limit:
            num = power
        result += num
    return result