def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])

"""
dp로 푸는 문제이다.
전에 행에서 현재 열을 제외한 다음의 수 중에서 가장 큰 값을 더하고 더해서 dp 테이블을 완성해서 리턴하는 식이다.
"""