def solution(s):
    text = s.split(" ")
    answer = []
    for t in text:
        word = ''
        for idx, s in enumerate(t):
            if idx % 2 == 0:
                word += s.upper()
            else:
                word += s.lower()
        answer.append(word)
    return " ".join(answer)

"""
그냥 string.split()과 string.split(" ")은 다르다
"Hello World"라는 문자열에서 ()으로 split을 하면 ["Hello", "World"]로 되지만 (" ")으로 하게 되면 ["Hello", " ", "World"]로 된다
난 처음에 위에 두 방식의 차이를 모르는체 계속 안되어서 조금 고생을 했다.
string.upper()를 사용하면 string를 대문자로, .lower()를 쓰면 소문자로 바꿔주는 형식의 함수들이다.
"""