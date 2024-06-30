def solution(strArr):
    answer = [len(i) for i in strArr]
    tmp = []
    for a in set(answer):
        tmp.append(answer.count(a))
    
    return max(tmp)