def solution(n,a,b):
    a,b = min(a,b), max(a,b)
    result = 1
    while not ( a % 2 == 1 and b % 2 == 0 and a + 1 == b):
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        result += 1
    
    return result