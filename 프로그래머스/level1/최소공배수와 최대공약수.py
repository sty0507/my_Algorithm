def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def solution(n, m):
    answer = []
    
    answer.append(gcd(n,m))
    answer.append(n * m / gcd(n, m))
    
    return answer

"""
유클리드 호제법을 사용해서 풀었다
a를 b로 나눈 나머지가 r이면 a,b의 최대공약수와 b,r의 최대 공약수는 같다는 것이다.
그렇게 해서 계속 수를 줄여가면서 결국 b가 0이 될때의 a의 값이 두 수의 최대 공약수가 되는 것이다.
최소 공배수는 두 수의 곱 나누기 두 수의 최대공약수 이기 때문에 그것을 이용했다.
"""