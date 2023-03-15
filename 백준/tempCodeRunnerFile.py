import sys
# 5로 나누어 떨어질때까지 2를 뺌

n = int(sys.stdin.readline())

def sol(n):
    result = 0
    
    while n != 0:
        if n%5 == 0:
            result += n/5
            n = n%5
        else:
            n -= 2
            result += 1

    if n <= 0:
        return -1
    else:
        return result

print(int(sol(n)))
