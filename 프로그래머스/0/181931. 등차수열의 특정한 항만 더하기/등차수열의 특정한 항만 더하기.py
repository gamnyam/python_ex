def solution(a, d, included):
    answer = 0
    num=[a]
    for i in range(1, len(included)):
        a+=d
        num.append(a)
    for i in range(len(included)):
        if included[i] == True:
            answer += num[i]
        
    return answer