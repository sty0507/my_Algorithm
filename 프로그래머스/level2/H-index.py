def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for h_count, i in enumerate(citations, start=1):
        h = max(h, min(h_count, i))
    return h