def solution(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    
    if x>= y :
        answer = x
    else :
        answer = y

    return answer

# 다른 풀이
def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a+b, b+a))
