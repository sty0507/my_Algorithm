def solution(cards1, cards2, goal):
    for data in goal:
        if cards1 and data == cards1[0]:
            del cards1[0]
        elif cards2 and data == cards2[0]:
            del cards2[0]
        else:
            return "No"
    return "Yes"