import sys
n = int(sys.stdin.readline())
arr = []
result = []
for i in range(1, n+1):
    arr.append(i)

while len(arr) != 1:
    result.append(arr.pop(0))
    arr.append(arr.pop(0))
result.append(arr.pop(0))

for i in result:
    print(i, end=' ')