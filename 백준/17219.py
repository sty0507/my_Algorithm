import sys

n, m = map(int, sys.stdin.readline().split())

password = {}

for i in range(n):
    k, v = sys.stdin.readline().split()
    password[k] = v

for i in range(m):
    search = sys.stdin.readline().rstrip()
    print(password[search])