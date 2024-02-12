def solution(seoul):
    for idx, s in enumerate(seoul):
        if s == "Kim":
            return f'김서방은 {idx}에 있다'