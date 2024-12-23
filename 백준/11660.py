import sys

N, M = map(int, sys.stdin.readline().split())
table = []
new_table = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        """
        if i != 1 and j != 1:
            new_table[i][j] = new_table[i-1][j] + new_table[i][j-1] + table[i-1][j-1] - new_table[i-1][j-1]
        elif j == 1 and i != 1:
            new_table[i][j] = new_table[i-1][j] + table[i-1][j-1]
        else:
            new_table[i][j] = new_table[i][j-1] + table[i-1][j-1]
        """
        new_table[i][j] = new_table[i][j-1] + new_table[i-1][j] - new_table[i-1][j-1] + table[i-1][j-1]
        # new_table에서의 i, j는 그대로 사용 가능
        # table에서는 i, j를 각각 -1을 해줘야 함

for _ in range(M):
    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
    
    result = new_table[x_2][y_2] - new_table[x_2][y_1-1] - new_table[x_1-1][y_2] + new_table[x_1-1][y_1-1]

    print(result)

"""
시간 초과 코드
for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    table.append(l)
    for j in range(N):
        new_table[i][j+1] = l[j] + new_table[i][j]

for _ in range(M):
    l = list(map(int, sys.stdin.readline().split()))
    x_1, y_1 = l[0], l[1]
    x_2, y_2 = l[2], l[3]
    if (x_1 == x_2) and (y_1 == y_2):
        print(table[x_1-1][y_1-1])
        continue
    default_row = [row[x_2] for row in new_table[y_1-1:y_2+1]]
    minus_row = [row[x_1-1] for row in new_table[y_1-1:y_2+1]]

    print(sum(default_row) - sum(minus_row))
"""

