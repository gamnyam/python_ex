def solution(my_string, is_suffix):
    if is_suffix in my_string[len(my_string)-len(is_suffix):] :
        answer = 1
    else :
        answer = 0
    return answer