# 내 코드
def solution(dartResult):
    dp = [0 for _ in range(int(len(dartResult) / 2))]
    idx = 0
    result = 0
    flag = False
    for i in range(len(dartResult)):
        d = dartResult[i]
        if not flag:
            if d.isdigit():
                if dartResult[i+1].isdigit():
                    dp[idx] = int(d + dartResult[i+1])
                    flag = True
                else:
                    dp[idx] = int(d)
                idx += 1
            elif d == "D":
                dp[idx-1] = dp[idx-1] ** 2
            elif d == "T":
                dp[idx-1] = dp[idx-1] ** 3
            elif d == "*":
                if (idx - 2) != -1:
                    dp[idx-2] *= 2
                    dp[idx-1] *= 2
                elif (idx - 1) != -1:
                    dp[idx-1] *= 2
            elif d == "#":
                if (idx - 1) != -1:
                    dp[idx-1] *= -1
        else:
            flag = False
        #print (dp, sum(dp), idx)
    return sum(dp)
"""
처음에 그냥 dp라는 배열을 안쓰고 풀려고 했는데 쉽지가 않았다.
*이 나오면 2번째 뒤에 것 까지 곱해줘야해서 관리?가 필요하다고 생각이 들어 배열을 사용해서 무지성 반복문으로 풀었다.
"""
# 다른 사람 코드
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
"""
정규표현식으로 사용해서 푼 코드이다. 참 똑똑한 것 같다.
"""