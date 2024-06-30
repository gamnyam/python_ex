def solution(myString, pat):
    answer =''
    end = myString.rfind(pat)
    answer = myString[:end+len(pat)]
    
    return answer