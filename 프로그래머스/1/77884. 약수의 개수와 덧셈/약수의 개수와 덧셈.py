def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        yak = []
        for i in range(1, num+1):
            if num % i == 0 :
                yak.append(i)
        if len(yak) % 2 == 0:
            answer += num
        else :
            answer -= num
    return answer