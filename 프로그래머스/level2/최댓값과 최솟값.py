def solution(s):
    answers = s.split(" ")
    answers = [int(a) for a in answers]
    answer = str(min(answers)) +" " + str(max(answers))
    return answer

"""
굳이 이렇게 반복문을 통해서 형 변환을 해주지 않고 map() 함수를 사용해도 된다.
answers = list(map(int, answers))
이런식으로
"""