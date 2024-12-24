import sys

N = int(sys.stdin.readline())

alpa = dict()

for _ in range(N):
    key, left, right = sys.stdin.readline().split()

    alpa[key] = [left, right]

def first_recursion(key):
    if key != ".":
        print(key, end="")
        first_recursion(alpa[key][0])
        first_recursion(alpa[key][1])

def middle_recursion(key):
    if key != ".":
        middle_recursion(alpa[key][0])

        print(key, end="")

        middle_recursion(alpa[key][1])

def last_recursion(key):
    if alpa[key][0] != ".":
        last_recursion(alpa[key][0])
    if alpa[key][1] != ".":
        last_recursion(alpa[key][1])
    
    print(key, end="")

first_recursion('A')
print()
middle_recursion('A')
print()
last_recursion('A')