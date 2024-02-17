from collections import deque
def solution(arr):
    answer = []
    answer.append(arr[0])
    queue = deque(arr)
    while queue:
        n = queue.popleft()
        if n != answer[-1]:
            answer.append(n)
    return answer