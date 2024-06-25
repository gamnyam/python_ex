def solution(a, b):
    if int(str(a) + str(b)) >= 2 * a * b :
        answer = int(str(a) + str(b))
    elif int(str(a) + str(b)) < 2 * a * b :    
        answer = 2 * a * b
    return answer