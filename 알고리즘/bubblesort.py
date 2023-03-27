import sys
n = int(sys.stdin.readline())
arr = [0] * 100
for i in range(n):
    arr[i] = int(sys.stdin.readline())

for j in range(n, 0, -1):
    for i in range(0, j-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

for i in range(n):
    print(arr[i])