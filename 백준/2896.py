import sys

buys = list(map(int, sys.stdin.readline().split()))
needs = list(map(int, sys.stdin.readline().split()))

mini = min(buys[0]/needs[0], buys[1]/needs[1], buys[2]/needs[2])

print(f"{buys[0]-needs[0]*mini: .6f} {buys[1]-needs[1]*mini: .6f} {buys[2]-needs[2]*mini: .6f}")