def solution(wallpaper):
    answer, location = [], []
    # x, y 값의 제일 큰 값과 작은 값을 각각 구하면 됨
    for i, wall in enumerate(wallpaper):
        for idx, sharp in enumerate(wall):
            l = []
            if sharp == "#":
                l.append(i)
                l.append(idx)
                location.append(l)
    location.sort(key=lambda y:y[0]) # y값을 기준으로 정렬
    x1 = location[0][0]
    y1 = location[-1][0] + 1
    location.sort(key=lambda x:x[1]) # x값을 기준으로 정렬
    x2 = location[0][1]
    y2 = location[-1][1] + 1
    answer.append(x1)
    answer.append(x2)
    answer.append(y1)
    answer.append(y2)
    return answer

# 다른 사람 풀이
def solution(wallpaper):
    x = []
    y = []
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]
