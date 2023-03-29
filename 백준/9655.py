import sys
n = int(sys.stdin.readline())
# 짝 : CY, 홀 : SK
th = int(n/3)
on = int(n%3)

if (th+on)%2 == 0:
    print("CY")
else:
    print("SK")