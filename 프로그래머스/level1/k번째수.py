def solution(array, commands):
    answer = []
    for command in commands:
        list = array[command[0] - 1 : command[1]]
        list = sorted(list)
        answer.append(list[command[2] - 1])
    return answer
