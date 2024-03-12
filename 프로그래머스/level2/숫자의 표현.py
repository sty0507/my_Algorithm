def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        sum = 0
        for j in range(i, n):
            sum += j
            if sum == n:
                answer += 1
                break
            if sum > n:
                break
    return answer

"""
처음에 그냥 n까지 i를 반복했더니 틀렸다고 떳었다.
간단하게 생각해보면 n이 20이라고 첬을 때 11만 되어도 그다음 수인 12와 더하면 절대로 20이 될 수 가 없기 때문에 반만해도 가능하다는 것이다.
"""