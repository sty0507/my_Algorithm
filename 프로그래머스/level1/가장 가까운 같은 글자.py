# 다른 사람 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
    return answer

# 내 풀이
def solution(s):
    inword, answer = [], []
    location = dict()
    for idx, string in enumerate(s):
        if string not in location:
            location[string] = idx
        if string in inword:
            answer.append(idx - location[string])
            location[string] = idx
        else:
            inword.append(string)
            answer.append(-1)
            location[string] = idx
    return answer
    