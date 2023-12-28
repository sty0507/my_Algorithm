# 도저히 못하겠어서 다른 사람 코드 사용함
def date_comparison(expiration_date, today):
    if expiration_date[0] > today[0]:
        return True
    if expiration_date[0] == today[0] and expiration_date[1] > today[1]:
        return True
    if expiration_date[0] == today[0] and expiration_date[1] == today[1] and expiration_date[2] > today[2]:
        return True
    return False

def solution(today, terms, privacies):
    result = []
    i = 1
    today = list(map(int,today.split(".")))

    expiration = {term[0]:int(term[2:]) for term in terms}
    for idx, pri in enumerate(privacies):
        pri = pri.split(" ")
        pri_date = list(map(int,pri[0].split(".")))

        pri_date[1] += expiration[pri[1]]

        if (pri_date[1] > 12):

            if (pri_date[1] % 12 == 0):
        
                pri_date[0] += (pri_date[1] // 12) - 1 
                pri_date[1] = 12

            else:
                pri_date[0] += pri_date[1] // 12
                pri_date[1] %= 12 

        if not date_comparison(pri_date, today) :
            result.append(idx+1)

    return result


"""
# 런타임 에러나는 코드
from datetime import datetime
def make_date(year, month, day):
    d = datetime(year, month, day)
    return d

def solution(today, terms, privacies):
    answer = []
    time = {}
    today = make_date(int(today[:4]), int(today[6:7]), int(today[8:11]))
    for item in terms:
        key, value = item.split()
        time[key] = int(value)
    for idx, p in enumerate(privacies):
        ty = p[-1]
        year = int(p[:4])
        month = int(p[5:7]) + time[ty]
        day = int(p[8:11]) - 1
        if day == 0:
            month -= 1
            day = 28
        if month > 12:
            year += 1
            month -= 12
        date = make_date(int(year), int(month), int(day))
        if  date < today:
            answer.append(idx+1)
    

    from collections import deque
    list = [5,3,6,1,2]
    print(list)
    list = deque(list)
    print(list)
    return answer

"""