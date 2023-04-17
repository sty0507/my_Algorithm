import sys
input = sys.stdin.readline

n = int(input())
fi = [0] * (n+2)
fi[0] = 0
fi[1] = 1
if n > 1:
    for i in range(2, n+1):
        fi[i] = fi[i-1] + fi[i-2]
print(fi[n]) 