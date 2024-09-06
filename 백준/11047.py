import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

cost = []
result = 0

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x <= k:
        cost.append(x)
cost.sort(reverse=True)
for i in range(len(cost)):
    if k == 0:
        break
    result += k / cost[i]
    k %= cost[i]

print(cost)