def solution(data, ext, val_ext, sort_by):
    answer = []
    label = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    key, so = label[ext], label[sort_by]
    for da in data:
        if da[key] < val_ext:
            answer.append(da)
    answer.sort(key=lambda x:x[so])
    return answer