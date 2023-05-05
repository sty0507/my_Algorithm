import sys
from collections import Counter
input = sys.stdin.readline
t = int(input())
arr = []
maxi = 1
for _ in range(t):
    n = int(input())
    arr.append(n)
arr.sort()
print(round(sum(arr) / t)) # 평균
print(arr[int(t/2)]) # 중앙값

# 최빈값
count_list = sorted(Counter(arr).items(), key = lambda x : (-x[1], x[0]))
if t == 1:
    print(arr[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

print(max(arr)-min(arr)) # 범위