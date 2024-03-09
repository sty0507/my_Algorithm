def solution(s):
    z = 0
    b = 0
    while s != "1":
        z += s.count("0")
        s = s.replace("0", "")
        s = format(len(s), 'b')
        b += 1
    return [b, z]