import sys

n = int(sys.stdin.readline())

moneys = list(map(int, sys.stdin.readline().rstrip().split()))

moneys.sort()
result = 0

for i in range(1, len(moneys)+1):
    result += sum(moneys[:i])

print(result)