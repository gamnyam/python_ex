def solution(a,b,c,d):
    counts = {}

    for num in [a,b,c,d] :
        if num in counts:
            counts[num] +=1
        else :
            counts[num] = 1

    values = list(counts.keys())
    freqs = list(counts.values())

    if len(values) == 1 :
        p = values[0]
        return 1111*p
        
    if 3 in freqs:
        p = values[freqs.index(3)]
        q = values[freqs.index(1)]
        return (10*p+q) ** 2
    
    if freqs.count(2) == 2:
        p = values[0]
        q = values[1]
        return (p+q) * abs(p-q)

    if 2 in freqs and freqs.count(1) == 2:
        p = values[freqs.index(2)]
        q = values[freqs.index(1)]
        r = values[freqs.index(1, freqs.index(1)+1)]
        return q*r

    if len(values) == 4:
        return min(values)