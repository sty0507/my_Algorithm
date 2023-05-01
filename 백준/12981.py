import sys
input = sys.stdin.readline

R, G, B = map(int, input().split())

small = min(R,G,B)
result = small
R,G,B = R-small, G-small, B-small

result += (R/3 + G/3 + B/3)
R,G,B = R%3, G%3, B%3

if R%2 == 1:
    result += 1
elif R/2 ==1:
    result += 1
elif G%2 == 1:
    result += 1
elif G/2 ==1:
    result += 1
elif B%2 == 1:
    result += 1
elif B/2 ==1:
    result += 1

print(int(result))