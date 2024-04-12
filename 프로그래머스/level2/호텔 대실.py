from heapq import heappush, heappop
def solution(book_time):
    books = []
    rooms = []
    for b in book_time:
        s, e = b
        sh, sm = s.split(":")
        eh, em = e.split(":")
        st, et = int(sh)*60+int(sm), int(eh) * 60 + int(em)
        heappush(books, [st,et])
    # 시작 시간과 끝나는 시간을 분으로 바꿔서 넣어준다.
    while books:
        st, et = heappop(books)
        if not rooms:
            rooms.append([et, st])
        else:
            room = heappop(rooms)
            if room[0] + 10 > st:
                heappush(rooms, room)
                heappush(rooms, [et, st])
            else:
                room = [et, st]
                heappush(rooms, room)
    return len(rooms)
"""
books라는 힙에 시작하는 시간과 끝나는 시간을 분으로 바꿔서 추가한다.
힙에서 하나씩 빼서 비교를 한다.
이번 대실 시간이 전에 대신 시간 + 10분 보다 작으면 아예 새 것을 추가
"""