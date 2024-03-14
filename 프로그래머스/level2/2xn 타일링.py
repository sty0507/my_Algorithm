def solution(n):
    dp =[0] * n
    dp[0] = 2
    dp[1] = 2
    dp[2] = 3
    for i in range(3, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n-1] 

"""
여기서 return dp[n-1] % 1000000007으로 하면 시간 초과가 뜬다.
그걸 피하기 위해서 dp에 넣을때부터 나머지를 구해준다.
"""