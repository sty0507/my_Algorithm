# 어느 정도는 맞지만 테케를 완벽히 통과 못한 코드
def solution(n, arr1, arr2):
    m = [[" " for _ in range(n)] for _ in range(n)]
    for idx, a in enumerate(arr1):
        b = format(a, 'b')
        if len(b) != n:
            b = "0" + b
        for i in range(len(b)):
            if b[i] == "1":
                m[idx][i] = "#"
    for idx, a in enumerate(arr2):
        b = format(a, 'b')
        if len(b) != n:
            b = ("0" * (n - len(b)) ) + b
        for i in range(len(b)):
            if b[i] == "1":
                m[idx][i] = "#"
    result = []
    for x in m:
        c = ""
        for i in x:
            c += i
        result.append(c)
    return result

# or 연산을 사용해서 푼 코드
def solution(n, arr1, arr2):
    m = [[" " for _ in range(n)] for _ in range(n)]
    arr = []
    for i in range(n):
        a = bin(arr1[i] | arr2[i])
        b = a[2:]
        if len(b) != n:
            b = ("0"*(n-len(b))) + b
        arr.append(b)
        
    result = []
    for i in range(n):
        r = ""
        for j in range(n):
            if arr[i][j] == "1":
                m[i][j] = "#"
            r += m[i][j]
        result.append(r)
    return result
                
"""
처음에 그냥 무지성 반복문으로 풀려고 했는데 테케에서 오류가 떠서 질문하기로 가서 질문들을 봤다.
나랑 같은 테케가 안되는 질문을 보는 중에 그냥 | 이거 하나를 봤는데 or 연산이 생각이 났다. 그래서 파이썬에서 or 연산을 해본 적이 없어,
하는 법을 찾아 본 후에 or 연산을 사용해서 풀었다.
솔직히 지금 코드를 더 줄여서도 짤 수 있을 거 같다. 하지만 나의 능력은 여기까지...
"""