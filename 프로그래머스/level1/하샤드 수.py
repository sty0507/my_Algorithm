def solution(x):
    num = [int(i) for i in str(x)]
    num = sum(num)
    if x % num == 0:
        return True
    else:
        return False