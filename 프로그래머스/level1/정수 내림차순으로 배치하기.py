# 내 코드
def solution(n):
    s = str(n)
    s1 = []
    for i in s:
        s1.append(int(i))
    s1.sort(reverse = True)
    s = ""
    for i in s1:
        s += str(i)
    return int(s)

# 다른 사람 코드
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))