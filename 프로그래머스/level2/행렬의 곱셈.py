def solution(arr1, arr2):
    answer = []
    for arr in arr1:
        l = []
        for a in range(len(arr2[0])):
            sum = 0
            for idx, n in enumerate(arr):
                sum += n * arr2[idx][a]
            l.append(sum)
        answer.append(l)
    return answer

"""
아마 파이썬에 존재하는 라이브러리를 사용하면 훨씬 더 짧고 간단하게 구현할 수 있을것인데 이걸 라이브러리를 사용할려고 하는게 아니다 보니 직접 풀어봤다.
일단 행렬의 곱셈은 간단하게 첫번째 행렬 테이블의 행과 두번째 행렬 테이블의 열과 하나씩 순서대로 곱한다음 더한 값이다.
그래서 그냥 첫번째 행렬 테이블의 행을 가져와서 두번째 행렬 테이블의 열의 개수 만큼 돌면서 곱한 값을 더하고 리스트에 담아서 리턴하는 형식이다.
처음에 그냥 인덱스 값으로만 할 생각을 하다가 좀 고민해서야 그냥 리스트를 받아서 쓰면 되겠다고 생각했다.
"""