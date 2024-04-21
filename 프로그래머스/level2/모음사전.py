from itertools import product
def solution(word):
    li = []
    w = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        for j in product(w, repeat = i):
            li.append(list(j))
            
    li.sort()
    answer = 0
    for wo in li:
        answer += 1
        wor = ''.join(s for s in wo)
        if (wor == word):
            break
    return answer

"""
문제 분류는 완전탐색으로 되어 있지만 그냥 수학으로도 풀 수 있는 문제이다. 뭐 다른 사람들 보니 ㄹㅇ 찐으로 자릿수의 값을 구해서 어떻게 하던데.
나는 그냥 중복순열을 사용해서 아예 사전을 만들고 비교하는 형식으로 했다.
"""