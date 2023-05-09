import sys
input = sys.stdin.readline
s1 = set()

m = int(input())

for _ in range(m):
    fun = list(input().strip().split())

    if len(fun) == 1:
        if fun[0] == "all":
            s1 = set([i for i in range(1, 21)])
        else:
            s1 = set()
    else:
        temp,x = fun[0], fun[1]
        if temp == "add":
            s1.add(x)
        elif temp == "check":
            if x in list(s1):
                print(1)
            else:
                print(0)
        elif temp == "remove":
            s1.discard(x)
        elif temp == "toggle":
            if x in (s1):
                s1.discard(x)
            else:
                s1.add(x)