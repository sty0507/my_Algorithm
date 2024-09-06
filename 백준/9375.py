import sys

T = int(sys.stdin.readline())

for _ in range(T):
    dic_type = dict()
    n = int(sys.stdin.readline())
    for i in range(n):
        name, type = sys.stdin.readline().strip().split()
        if type not in dic_type.keys():
            dic_type[type] = 0
        dic_type[type] += 1

    cnt = 1
    if len(dic_type.keys()) == 1: # 입력으로 들어 온 것들이 모두 같은 종류일 경우
        print(n)
    else:
        for d in dic_type.keys():
            cnt *= (dic_type[d] + 1)
        print(cnt - 1)