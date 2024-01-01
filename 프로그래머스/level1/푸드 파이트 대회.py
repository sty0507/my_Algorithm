def solution(food):
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] = food[i] - 1
    answer = ''
    for idx, cnt in enumerate(food):
        if idx != 0:
            for i in range(int(cnt / 2)):
                answer += str(idx)
    left = answer[::-1]
    answer += '0' + left
    return answer