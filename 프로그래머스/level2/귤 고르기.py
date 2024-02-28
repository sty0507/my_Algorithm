from collections import Counter
def solution(k, tangerine):
    result = 1
    tangerine.sort()
    counter = Counter(tangerine)
    values = sorted(list(counter.values()), reverse=True)
    l = len(values)
    
    sum = 0
    for i in range(l):
        sum += values[i]
        if sum >= k:
            return result
        result += 1

"""
일단 Counter 라이브러리를 사용한다.
인자로 넘긴 받은 리스트에서 같은 값들의 개수를 딕셔너리로 넘겨준다. 그래서 처음에 중복이 있는 리스트를 입력 받기 때문에 중복된 개수를 구한다.
그리고 딕셔너리이니깐 .value만 뽑아서 리스트로 바꿔준 다음 정렬을 해준다.
sorted()로 하면 오름차순으로 정렬이 된다.
그리고 반복문으로 거꾸로 돌면서 sum이라는 변수에 넣어서 원하는 값이랑 같아지거나 넘으면 리턴을 해주는 그림이다.

문제를 보면 귤 크기가 일정한 것을 원하니 비슷한게 많은 순으로 하면 된다.
"""