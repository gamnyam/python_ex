def solution(name, yearning, photo):
    answer = []
    for now_photo in photo :
        score = 0
        
        for target_person in now_photo:
            for i, target_name in enumerate(name):
                if target_person == target_name :
                    score += yearning[i]
                    break
        answer.append(score)
    return answer