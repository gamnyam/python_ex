def solution(myString):
    alp_list = ["a","b","c","d","e","f","g","h","i","j","k"]
    answer = myString
    for alp in alp_list:
        if alp in myString: 
            answer = answer.replace(alp, "l")
    return answer