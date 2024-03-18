def solution(n):
    dp = [0] * (n+4)
    dp[2] = 3
    dp[4] = 11
    for i in range(5, n + 1):
        if i % 2 == 0:
            dp[i] = ((dp[i-2] * 4) - (dp[i-4])) % 1000000007
    return dp[n]

"""
점화식만 구하면 dp든 어떻게든 풀 수 있는 문제이다.
2 : 3, 4 : 11, 6 : 41이여서 점화식은 f(n) = f(n-2) * 4 - f(n-4) 단, n은 짝수 와 같이 식을 세울 수 있다.
그래서 나는 그냥 dp로 풀었다.
"""