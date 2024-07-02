def solution(a, b, c, d):
    # 주사위 숫자의 빈도를 계산
    counts = {}
    for num in [a, b, c, d]:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # 빈도별 숫자를 추출
    values = list(counts.keys())
    freqs = list(counts.values())

    # 네 주사위가 모두 같은 경우
    if len(values) == 1:
        p = values[0]
        return 1111 * p
    
    # 세 주사위가 같고 나머지 하나가 다른 경우
    if 3 in freqs:
        p = values[freqs.index(3)]
        q = values[freqs.index(1)]
        return (10 * p + q) ** 2
    
    # 두 개씩 같은 값이 나오는 경우
    if freqs.count(2) == 2:
        p = values[0]
        q = values[1]
        return (p + q) * abs(p - q)
    
    # 두 주사위가 같은 값이 두 쌍 존재하는 경우
    if 2 in freqs and freqs.count(1) == 2:
        p = values[freqs.index(2)]
        q = values[freqs.index(1)]
        r = values[freqs.index(1, freqs.index(1) + 1)]
        return q * r
    
    # 네 주사위의 숫자가 모두 다른 경우
    if len(values) == 4:
        return min(values)