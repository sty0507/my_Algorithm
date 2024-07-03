import sys
n, m = map(int, sys.stdin.readline().split())
six = []
per = []
for i in range(m):
    s, p = map(int, sys.stdin.readline().split())
    six.append(s)
    per.append(p)

s_min = min(six)
p_min = min(per)

if s_min < (p_min * 6):
    if s_min < ((n % 6) * p_min):
        print((n // 6) * s_min + s_min)
    else:
        print((n // 6) * s_min + (n % 6) * p_min)
        
elif s_min >= p_min * 6:
    print(n * p_min)
