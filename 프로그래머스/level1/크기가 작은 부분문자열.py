def solution(t, p):
    length = len(p)
    l = len(t)
    result = 0
    for i in range(l - length + 1):
        if t[i:i+length] <= p:
            result += 1
    return result