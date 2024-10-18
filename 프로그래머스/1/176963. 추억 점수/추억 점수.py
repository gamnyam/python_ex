def solution(name, yearning, photo):
    
    answer = []
    name2score = dict(zip(name, yearning))
    
    for names in photo:
        score = 0
        for name in names :
            score += name2score.get(name,0)
        answer.append(score)
    return answer