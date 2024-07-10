import sys

n = sys.stdin.readline()

total = [int(n[i]) for i in range(len(n) - 1)]

cnt = 0

while True:
    if sum(total) // 10 == 0:
        break
    s = str(sum(total))
    total = [int(s[i]) for i in range(len(s))]
    cnt += 1

if cnt != 0:
    cnt += 1

print(cnt)

if sum(total) % 3 == 0:
    print("YES")
else:
    print("NO")