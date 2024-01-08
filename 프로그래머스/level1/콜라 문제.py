def solution(a, b, n):
    answer = 0
    while n >= a:
        num1 = int(n / a) * b
        num2 = int(n % a)
        n = num1 + num2
        answer += num1
    return answer