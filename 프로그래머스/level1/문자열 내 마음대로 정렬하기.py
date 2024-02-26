def solution(strings, n):
    result = sorted(strings, key=lambda s:(s[n],s))
    return result
        
"""
간단하게 sorted() 함수를 사용했다.
sorted() 함수의 파라미터로 key의 값을 지정해주면 그것으로 정렬을 해준다.
그래서 여기서는 lambda를 사용해서 기본으로 s[n] 정렬 기준으로 한다. 그런데 만약 같다면 다른 기준으로 s를 기준으로 정렬을 한다.
그렇게 정렬을 해서 리턴을 하는 코드이다.
lambda 매개변수 : 표현식
"""