def solution(babbling):
    says = ["aya", "ye", "woo", "ma"]
    result = []
    answer = []
    for data in babbling:
        num = 0
        for say in says:
            if say * 2 in data:
                num = 0
            elif say in data:
                data = data.replace(say, '*')
        if all(ch == '*' for ch in data):
            num += 1
            result.append(num)
    return sum(result)

# 메인 아이디어는 줄줄이 나오지 않게 찾는 것!
# 8번째 줄에서 say * 2가 줄줄이 나오는 것을 체크
# 12번째 줄에서 all() 함수를 사용해서 True or False를 체크