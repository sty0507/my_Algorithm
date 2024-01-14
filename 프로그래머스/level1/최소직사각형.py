def solution(sizes):
    big_list = []
    small_list = []
    for size in sizes:
        if size[0] > size[1]:
            big_list.append(size[0])
            small_list.append(size[1])
        else:
            big_list.append(size[1])
            small_list.append(size[0])
    return max(big_list) * max(small_list)
        