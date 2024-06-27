def solution(myString, pat):
    str = myString.lower()
    p = pat.lower()
    if p in str :
        answer = 1
    else:
        answer = 0
    return answer