import sys
input = sys.stdin.readline

n,k = map(int, input().split())
man = [[0],[0],[0],[0],[0],[0]]
woman = [[0],[0],[0],[0],[0],[0]]
def make(people):
    x = 0
    for i in range(6):
        x += int(people[i][0]/k)
        x += int(people[i][0]%k)
    return x
for i in range(n):
    s,y = map(int, input().split())
    if s == 0:
        woman[y-1][0] += 1
    else:
        man[y-1][0] += 1


print(make(man) + make(woman))