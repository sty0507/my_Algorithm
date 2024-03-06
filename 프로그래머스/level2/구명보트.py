def solution(people, limit):
    answer = 0
    people.sort()
    front, end = 0, len(people)-1
    
    while front <= end:
        if people[front] + people[end] <= limit:
            front +=1
        end -= 1
        answer += 1
    return answer