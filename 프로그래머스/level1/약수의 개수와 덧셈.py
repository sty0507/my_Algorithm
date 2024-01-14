import math
def solution(left, right):
    odd = 0
    even = 0
    for num in range(left, right + 1):
        n = 0
        # 약수의 개수 구하기
        for i in range(1, int(math.sqrt(num)) + 1):
            if int(num % i) == 0:
                n += 1
                if (i**2) != num:
                    n += 1
        if n % 2 == 0:
            even += num
        else:
            odd += num
    return even - odd

# 시간 초과를 안걸리기 위해서 sqrt(), 제곱근을 활용한것
# 두자리수 정도까지는 그냥 해도 상관이 없지만 그를 넘어가는 수는 꽤 오래 걸린다.
# 그래서 제곱근을 활용하는 것이다.
# 약수는 짝을 갖는다. 짝이 같은 수 일수도 있지만 쩻든 짝을 같기 때문에 약수의 수를 구하려는 수의 반의 값만 사용해서 그의 짝을 찾는 방식으로해서 시간초과를 없앤다.