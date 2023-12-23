def solution(name, yearning, photo):
    answer = []
    point = dict(zip(name, yearning))
    for p in photo:
        score = 0
        for i in p:
            if i in point:
                score += point[i]
        answer.append(score)
    return answer