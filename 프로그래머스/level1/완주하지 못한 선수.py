# 테스트 케이스는 통과하지만 효율성 검사를 통과 못한 코드
def solution(participant, completion):
    for com in completion:
        participant.remove(com)
    return participant[0]

# 효율성까지 통과한 코드
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for part, com in zip(participant, completion):
        if part != com:
            return part
    return participant[-1]
# 두 리스트를 모두 정렬을 해줘서 인덱스 값으로 비교를 한다.
# 같은 인덱스 값에 있어야 한다. 하지만 다른 값일 경우는 completion에 없는 값이기 때문에 그 값을 리턴을 한다.
# 넘겨 받은 두 리스트의 길이가 같을 경우 동명이인이 있다는 건데 그러면 반복문을 통해 걸러졌던가 아니면 제일 뒤에 있는 경우이다.

# 다른 사람이 짠 코드
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]