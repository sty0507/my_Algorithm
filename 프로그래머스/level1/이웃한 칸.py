def solution(board, h, w):
    answer, here, max_x, max_y = 0, board[h][w], len(board[0]) - 1, len(board) - 1
    list_x = [1,-1, 0, 0]
    list_y = [0, 0, 1, -1]
    for i in range(4):
        x = h + list_x[i]
        y = w + list_y[i]
        if (0 <= x <= max_x) and (0 <= y <= max_y):
            answer += int(board[x][y] == here)
    return answer
