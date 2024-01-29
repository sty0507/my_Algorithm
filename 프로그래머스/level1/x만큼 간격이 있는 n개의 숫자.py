def solution(x, n):
    result = [x]
    for i in range(n-1):
        result.append(result[i] + x)
    return result