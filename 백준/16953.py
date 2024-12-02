import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

"""
나름 제대로 풀었지만 시간 초과
results = 0
while b > a:
    if (b % 10) == 1:
        b = b // 10
        results += 1
    
    if (b % 2) == 0:
        b = b // 2
        results += 1

if b == a:
    print(results + 1)
else:
    print(-1)
"""

def dfs_1(a, b):
    queue = deque()
    queue.append((b, 1))

    while queue:
        n, t = queue.popleft()

        if n < a:
            continue

        if n == a:
            print(t)
            return
        
        if (n % 10) == 1:
            queue.append((n // 10, t+1))
        if (n % 2) == 0:
            queue.append((n // 2, t+1))
    print(-1)

dfs_1(a,b)