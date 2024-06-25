def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        answer = 1
    else :
            answer = 0
    
    return answer

# 다른 풀이
def solution(number, n, m):
    if number % n == 0 :
        if number % m == 0 :
            answer = 1
        else :
            answer = 0
    elif number % n == 0 & number % m == 0 :
        answer = 1
    else :
        answer = 0
    return answer
