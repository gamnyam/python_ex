def solution(num_list):
    if len(num_list) >= 11 :
        return sum(num_list)
    elif len(num_list) <= 10 :
        answer = 1
        for i in num_list:
            answer *= i
    return answer