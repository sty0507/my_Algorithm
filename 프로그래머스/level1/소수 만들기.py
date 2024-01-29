def solution(nums):
    l = len(nums)
    three = []
    result = []
    for i in range(l):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                three.append(nums[i] + nums[j] + nums[k])
    for t in three:
        if all(t%i != 0 for i in range(2, t)):
            result.append(t)

    return len(result)

# 더해야할 수들의 개수가 정해졌기 때문에 무지성 반복문이 가능하다
# 더해서 그 값들이 소수인지 판별하는 법은 소수는 약수로 자신과 1만을 가져야하기 때문에 그 사이의 숫자로 해당하는 값을 나눴을때 모든 값의 나머지가 0이 아니면 그 값은 소수인 것이다.