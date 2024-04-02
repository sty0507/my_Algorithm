# 오답이지만 기본 테케는 통과한 코드
def solution(s):
    l = len(s)-1
    i = 0
    while i < l:
        if s == "":
            return 1
        if s[i] == s[i+1]:
            s = s.replace(s[i],'',1)
            s = s.replace(s[i], '',1)
            i = 0
        else:
            i += 1
    return 0

# 정답코드
def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if len(stack) > 0 and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    
    if len(stack) != 0:
        return 0
    else:
        return 1
        
"""
처음에 무지성으로 반복문을 써서 풀어봤다. 나름 테케도 통과하고 잘 짜여졌지만 제출을 하니 제출 테케에서 런타임 에러가 떳다.
그래서 질문하기에 들어갔더니 모두가 스택을 왜치고 있어서 바로 스택으로 풀었다. 확실히 스택으로 푸는게 더 쉽고 간결하고 효율적인것 같다.
"""