def solution(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    
    if x>= y :
        answer = x
    else :
        answer = y

    return answer