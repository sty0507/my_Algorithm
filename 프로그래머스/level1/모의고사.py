def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    students = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        if student1[idx % len(student1)] == ans:
            students[0] += 1
        if student2[idx % len(student2)] == ans:
            students[1] += 1
        if student3[idx % len(student3)] == ans:
            students[2] += 1
    
    for idx, m in enumerate(students):
        if max(students) == m:
            answer.append(idx+1)
    return answer            