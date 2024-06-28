def solution(n):
    l = range(n)
    answer = []
    for i in l :
        ans = []
        for j in l:
            if i == j :
                ans.append(1)
            else:
                ans.append(0)
        answer.append(ans)
   
    return answer