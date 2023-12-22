from collections import deque

def solution(bandage, health, attacks):
    attacks = deque(attacks)
    end = attacks[-1][0]
    seq, max_health = 0, health
    for t in range(1, end + 1):
        if health <= 0:
            return - 1
        if not attacks:
            break
        seq += 1
        if t == attacks[0][0]:
            health -= attacks.popleft()[1]
            seq = 0
        elif seq == bandage[0]:
            health += bandage[1] + bandage[2]
            seq = 0
        else:
            health += bandage[1]
            
        if health > max_health:
            health = max_health
            
    return health if health > 0 else -1