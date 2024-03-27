def solution(N, stages):
    stage = [0] * N
    persent = [0] * N
    l = len(stages)
    for s in stages:
        if s <= N:
            stage[s-1] += 1
    persent[0] = (stage[0] / l) * 100
    if persent[0] == 100:
        return list(i for i in range(1, N+1))
    for i in range(1, len(stage)):
        if (l - stage[i-1] == 0):
            continue
        persent[i] = stage[i] / (l - stage[i-1]) * 100
        stage[i] += stage[i-1]
    indexed_data = [(index+1, value) for index, value in enumerate(persent)]
    sorted_data = sorted(indexed_data, key = lambda x : (-x[1], x[0]))
    result = [item[0] for item in sorted_data]
    return result

"""
dp? 느낌으로 했다. 각 스테이지는 결국 "클리어 못한 플레이어 / 스테이지에 도달하거나 지난 플레이어"의 퍼센트이기 때문에 전 스테이지에 있던 사람의 수를 전체에서 빼는데, 
계속 그 자리로 더해가는 식으로 했다.
dp[0] = 1, dp[1] = 3, dp[2] = 4면
dp[1]의 연산을 할 때 dp[0]의 값을 사용하고 끝나면 dp[1] += dp[0], 15번째 줄과 같이 했다.
그래서 결국에는 dp[0] = 1, dp[1] = 4, dp[2] = 8과 같은 식으로 해서 그 스테이지를 지나간 사람의 수를 구했다.
그리고는 그냥 비교해서 내림차순으로 된 리스트를 만들었다.
"""