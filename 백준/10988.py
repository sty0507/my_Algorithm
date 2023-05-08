import sys
input = sys.stdin.readline

s = input()
s = list(s)
s1 = list(s)
s.pop(-1)
s = ''.join(s)
s1.pop(-1)
s1.reverse()
s1 = ''.join(s1)
if s == s1:
    print(1)
else:
    print(0)