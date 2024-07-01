def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if set(str(i)).issubset({"0","5"}):
            answer.append(i)
    return answer or [-1]