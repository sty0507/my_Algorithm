def solution(n, lost, reserve):
    twin = set(lost) & set(reserve) # 여벌 옷 + 도난
    lost = sorted(list(filter(lambda x : x not in twin, lost)))
    reserve = sorted(list(filter(lambda x : x not in twin, reserve)))
    for l in lost:
        if (l-1) in reserve:
            reserve.remove(l-1)
        elif (l+1) in reserve:
            reserve.remove(l+1)
        else:
            n -= 1
    return n

"""
반복문을 통해서 값이 리스트에 값이 있는지를 확인 후에 총 개수에서 빼기를 해주는 형식이다.
반복문에 있는 조건문을 통해 빌릴 수 있냐를 확인하는 것이고 빌릴게 없다면 전체 인원에서 마이너스 하는 형식이다.

twin 변수는 set()을 사용해서 겹치는 수 없애고 and 연산(&)을 통해서 여벌 옷도 있지만 도난 당한 학생의 수를 구하는 변수이다.
그리고 lost와 reserve 변수는 기존에 입력 받았던 값에서 twin 값을 빼고 정렬하는 코드이다.
lambda는 lambda 매개변수 : 표현식 이다. - x가 twin에 있는지를 확인한다.
filter()는 첫번째 인자는 필터링을 할 함수가 들어가고(그래서 lanbda가 들어간다.) 두번째 인자에는 반복 가능한 인자가 들어간다.
그러니 lambda의 x 값은 각각 lost, reserve 의 값이다. 그 값이 twin에 없으면 각각의 변수에 들어가는 형태이다.
"""