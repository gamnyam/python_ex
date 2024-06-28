def solution(my_string, is_prefix):
    
    if is_prefix in my_string[0:len(is_prefix)]:
        answer = 1 
    else :
        answer = 0
        
    return answer