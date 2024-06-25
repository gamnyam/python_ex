def solution(num_list):
    a = sum(num_list)**2
    ans = 1
    for b in num_list :
        ans *= b
    if ans < a :
        answer = 1
    else :
        answer = 0

    return answer