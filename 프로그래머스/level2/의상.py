def solution(clothes):
    di = {}
    n = 1
    for c in clothes:
        if c[1] in di:
            di[c[1]] += 1
        else:
            di[c[1]] = 2
    if len(di.keys()) == 1:
        return sum(di.values()) - 1
    for d in di:
        n *= di[d]
    return n - 1
    

"""
수학적 문제이다. (a+1)..(n+1) - 1라는 수식을 얻는 것이 중요한다.
의상이 하나씩 있다고 할때 a의 의상과 b의 의상으로 얻을 수 있는 것은 a, b, ab이다. 이것은 (a+1)(b+1) - 1과 같다. 결국은 수학 공식이다.
그래서 딕셔너리로 의상 종류의 개수를 구해서 위의 공식으로 풀면 되는 문제이다.
"""