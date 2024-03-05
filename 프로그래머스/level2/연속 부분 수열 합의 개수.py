# 내가 짠 코드
def solution(elements):
    l = len(elements)
    elements = elements * 2
    answer = []
    for i in range(l):
        for j in range(l):
            answer.append(sum(elements[j:j+i]))
    answer = set(answer)
    return len(answer)
    
"""
처음에 반복문을 통해서 풀려했지만 나의 머리로는 살짝 힘들었다. 하지만 어느정도 구현을 했다.
일단 반복문을 통해서 elements의 크기를 넘어갔을 때 마지막 인자와 처음 인자를 더해야하는 때를 구할려했다.
그런데 리스트를 계속 보니 어떻게 하면 곱하기 2를 하면 똑같은 결과를 낼 수 있다는 걸 생각했다.
그래서 곱해서 2번 반복하도록 한 다음 반복문을 통해서 더한 값을 answer 리스트에 담는다.
그리고 파이썬에 있는 집합, set()을 사용해서 중복 값을 제거한 다음 집합의 개수를 리턴하도록 코드를 작성했다.
다른 사람들의 코드를 보니 대부분 set()을 처음부터 사용을 했다.
"""

# 다른 사람 코드
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)

"""
일단 set()을 먼저 선언하고, 반복문을 돈다.
일단 기본 값을 넣고 그 값 부터 최대 길이, ll를 더함으로써 끝까지 돈다.
ex [1 2 3 4]에서 i가 1이면 반복문이 [2 3 4 5]까지 돔. 그런데 5자리는 없는 자리니깐 밑에서 나머지 연산을 사용해서 1로 넘기는 거임
그렇게 집합에 넣어서 구함
이게 확실히 속도 면에서는 더 빠를거 같다.
실행해보니 거의 10배? 5배? 가량 더 빠른거 같다.
"""