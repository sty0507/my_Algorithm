def solution(keymap, targets):
    alpa = {}
    answer = []
    for al in keymap:
        for idx, data in enumerate(al):
            if data in alpa and alpa[data] <= idx:
                continue
            else:
                alpa[data] = idx + 1
    for data in targets:
        result = 0
        for d in data:
            if d in alpa:
                result += alpa[d]
            else:
                result = -1
                break
        answer.append(result)
    return answer

"""
파이썬의 딕셕너리를 사용해서 알파벳을 키 값으로 잡고 그 알파벳의 위치를 딕셔너리의 value 값으로 잡아서 문제를 푼다
"""