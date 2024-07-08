import sys

n, k, m = map(int, sys.stdin.readline().split())

total = 0

while k != m:
    k -= k // 2
    m -= m // 2
    total += 1

print(total)