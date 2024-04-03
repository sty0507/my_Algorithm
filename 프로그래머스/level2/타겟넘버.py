def solution(numbers, target):
    global answer
    answer = 0
    def dfs(x, i):
        if i == len(numbers):
            if x == target:
                global answer
                answer += 1
            return
        dfs(x + numbers[i], i+1)
        dfs(x - numbers[i], i+1)
        return
    dfs(0, 0)
    return answer