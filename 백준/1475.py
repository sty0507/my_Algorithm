import sys
input = sys.stdin.readline

n = str(input().strip())
arr = [0] * 10
l = len(n)

for i in range(l):
    num = int(n[i])
    if num == 6 or num == 9:
        if arr[6] >= arr[9]:
            arr[9] += 1
        else:
            arr[6] += 1
    else:
        arr[num] += 1

print(max(arr))