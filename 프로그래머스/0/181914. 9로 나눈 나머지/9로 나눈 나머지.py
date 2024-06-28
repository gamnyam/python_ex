def solution(number):
    answer = 0
    for i in range(0, len(number)) :
        answer = (answer + int(number[i]))%9
    return answer