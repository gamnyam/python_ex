def solution(myString, pat):
    answer = int(pat.lower() in myString.replace("A","b").replace("B","a"))
    return answer