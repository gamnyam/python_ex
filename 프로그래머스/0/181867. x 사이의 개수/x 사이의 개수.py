def solution(myString):
    answer = []
    b = myString.split("x")
    for i in b :
        answer.append(len(i))
    return answer