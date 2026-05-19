def solution(answers):
    answer = []
    score = [0, 0, 0]
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, ans in enumerate(answers):
        if ans == student1[i % len(student1)]:
            score[0] += 1
        if ans == student2[i % len(student2)]:
            score[1] += 1
        if ans == student3[i % len(student3)]:
            score[2] += 1
    
    max_score = max(score)
    
    for idx, s in enumerate(score):
        if s == max_score:
            answer.append(idx + 1)
    
    return answer