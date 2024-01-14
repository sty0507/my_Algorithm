def solution(s):
    numbers = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "zero" : "0"}
    
    for num in numbers:
        if num in s:
            s = s.replace(num, numbers[num])
    return int(s)

# str.replace()를 사용할때 변수에 담아야한다.
# 그것도 모르고 s.replace()만 쓰고 계속 안되서 개고생을 했다.