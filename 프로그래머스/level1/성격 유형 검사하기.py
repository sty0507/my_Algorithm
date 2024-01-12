def solution(survey, choices):
    answer = ''
    points = [3,2,1,0,1,2,3]
    emo = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    key = list(emo.keys())
    for idx, sur in  enumerate(survey):
        if choices[idx] > 4:
            emo[sur[1]] += points[choices[idx] - 1]
        else:
            emo[sur[0]] += points[choices[idx] - 1]
    
    for i in range(0, len(key), 2):
        if emo[key[i]] > emo[key[i+1]] or emo[key[i]] == emo[key[i+1]]:
            answer += key[i]
        else:
            answer += key[i+1]
    return answer
        
