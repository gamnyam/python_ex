def solution(numLog):
    answer = ''
    for i in range(0, len(numLog)-1):
        if numLog[i+1]-numLog[i] == 1:
            answer = answer + "w"
        elif numLog[i+1]-numLog[i] == -1:
            answer = answer + "s"
        elif numLog[i+1]-numLog[i] == 10:
            answer = answer +"d"
        elif numLog[i+1]-numLog[i] == -10:
            answer = answer +"a"

    return answer