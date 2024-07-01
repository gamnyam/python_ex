def solution(rank, attendance):
    ps = []
    for i in range(len(rank)):
        if attendance[i] == True:
            ps.append((rank[i],i))
    ps.sort()
    
    top3=[]
    for student in ps[:3]:
        top3.append(student[1])
    answer = 10000*top3[0] + 100*top3[1]+top3[2]
    
    return answer