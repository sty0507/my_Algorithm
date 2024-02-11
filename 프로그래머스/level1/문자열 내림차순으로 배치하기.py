def solution(s):
    answer = ''
    st = [i for i in s]
    st.sort(reverse = True)
    for i in st:
        answer += i
    return answer