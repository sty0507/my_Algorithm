# 나의 풀이
def solution(absolutes, signs):
    for idx, sign in enumerate(signs):
        if not sign:
            absolutes[idx] *= -1
    return sum(absolutes)

# 다른 사람 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
