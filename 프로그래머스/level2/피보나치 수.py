def solution(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n] % 1234567

"""
처음에 재귀로 풀었는데 테케 통과를 못했다.
시간을 넘었다나 뭐라나. 그래서 재귀보단 시간복잡도가 작은 dp를 활용해서 풀었다.
"""