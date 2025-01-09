import sys

N = int(sys.stdin.readline())

fact = 1

for i in range(1, N+1):
    fact *= i

fact = str(fact)

result = 0

for i in range(len(fact)-1, 0, -1):
    if fact[i] == "0":
        result += 1
    else:
        break

print(result)