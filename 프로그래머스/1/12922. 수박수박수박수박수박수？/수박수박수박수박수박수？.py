def solution(n):
    answer = ''
    while True :
        answer+='수'
        if n == len(answer) :
            break
        answer+='박'
        if n == len(answer) :
            break
    return answer