def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum

"""
작은 수로 만들어야하기 때문에 제일 큰 값을 제일 작은 값과 곱해주면 된다.
그래서 sort()를 사용해서 정렬을 오름차순이랑 내림차순으로 해주고 곱하는 식으로 했다.
아마 반복문을 안쓰고도 다른 방법이 있을 것 같다.
"""