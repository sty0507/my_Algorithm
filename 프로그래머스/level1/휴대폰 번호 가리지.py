# 나의 코드
def solution(phone_number):
    last = phone_number[-4:]
    number = ''
    for n in range(len(phone_number) - len(last)):
        number += "*"
    return number + last

# 다른 사람 코드
def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]

"""
나의 코드를 훨씬 더 간결하게 한 코드인거 같다.
* 하면 된다는 것을 몰랐다.
"""