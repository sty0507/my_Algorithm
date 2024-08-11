import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

members = {}

result = []

for _ in range(n):
    member = sys.stdin.readline().rstrip()
    members[member] = 1

for _ in range(m):
    member = sys.stdin.readline().rstrip()
    if member in members:
        members[member] += 1
    else:
        members[member] = 1

for key, value in members.items():
    if value == 2:
        result.append(key)

result.sort()
print(len(result))
for r in result:
    print(r)