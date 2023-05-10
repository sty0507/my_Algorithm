import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = [i for i in range(2, n+1)]
de = []
while len(de) < k:
    i = 0
    p = min(arr)
    l = len(arr)
    while l > 0:
        if arr[i]%p == 0:
            de.append(arr[i])
            arr.remove(arr[i])
            l -= 1
        i += 1
        l -= 1
print(de[k-1])