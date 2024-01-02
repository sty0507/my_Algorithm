# 내 코드
def solution(k, score):
    answer = []
    test = []
    for i in score:
        test.append(i)
        test.sort()
        if len(test) < k:
            answer.append(test[0])
        else:
            a = test[-k:-k + 1][0]
            answer.append(a)
    return answer


# 다른 사람 코드
def solution(k, score):
    result = []
    k_scores = []

    for i in score: 
        k_scores.append(i)
        k_scores.sort(reverse=True)
        if len(k_scores) > k:
            k_scores.pop()
            result.append(k_scores[-1])

    return result