import sys
input = sys.stdin.readline
board = []
for i in range(8):
    s = list(input())
    s.pop()
    board.append(s)

result = 0
for i in range(8):
    for j in range(8):
        if (i % 2 == 0):
            if (j % 2 == 0):
                if board[i][j] == 'F':
                    result += 1
        else:
            if j % 2 != 0:
                if board[i][j] == 'F':
                    result += 1

print(result)
