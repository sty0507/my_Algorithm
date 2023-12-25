def solution(n, m, section):
    answer = 1
    start = section[0]
    for i in section:
        if start + (m-1) < i:
            start = i
            answer += 1
    return answer
"""
section의 제일 처음 값의 m-1을 더한 값 보다 다음 section 값이 크다면 answer에 값 증가
"""