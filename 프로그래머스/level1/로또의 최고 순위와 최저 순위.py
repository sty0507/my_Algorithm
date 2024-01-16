def ranking(data):
    if data == 6:
        return 1
    elif data == 5:
        return 2
    elif data == 4:
        return 3
    elif data == 3:
        return 4
    elif data == 2:
        return 5
    else:
        return 6
def solution(lottos, win_nums):
    result = 0
    answer = []
    for lotto in lottos:
        if lotto in win_nums:
            result += 1
    top = result + lottos.count(0)
    
    answer.append(ranking(top))
    answer.append(ranking(result))
    
    return answer

# 다른 사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
    # 랭킹을 굳이 찾지 않고 리스트로 랭킹을 만들어서 사용한 점에서 훨씬 깔끔해지고 가독성도 높아진거 같다.