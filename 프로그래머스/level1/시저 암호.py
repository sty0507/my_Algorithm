# 런타임 에러가 나는 코드
def solution(s, n):
    alpa_small =[chr(i) for i in range(97,123)] # 소문자 알파벳 생성
    alpa_big = [chr(i) for i in range(65, 90)] # 대문자 알파벳 생성
    answer = ''
    idx = 0
    for i in s:
        if i in alpa_small:
            idx = alpa_small.index(i) + n
            if idx > 25:
                idx -= 26
            answer += alpa_small[idx]
        elif i in alpa_big:
            idx = alpa_big.index(i) + n
            if idx > 25:
                idx -= 26
            answer += alpa_big[idx]
        else:
            answer += i
    return answer

# 통과한 코드
def solution(s, n):
    answer = ''
    for i in s:
        if 65 <= ord(i) and ord(i) <= 90 :
            idx = ord(i) + n
            if idx > 90:
                idx -= 26
            answer += chr(idx)
        elif 97 <= ord(i) and ord(i) <= 122:
            idx = ord(i) + n
            if idx > 122:
                idx -= 26
            answer += chr(idx)
        else:
            answer += i
    return answer

"""
런타임 에러가 났던 이유는 처음에 알파벳 소문자와 대문자를 담은 리스트를 생성하는데 시간이 오래 걸려서 인것 같다.
문자의 아스키코드 값을 이용하면 풀 수 있는 것이다.
"""