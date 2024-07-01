def solution(arr, k):
    answer = []
    seen = set()
    
    for i in arr:
        if i not in seen:
            answer.append(i)
            seen.add(i)
        if len(answer)==k:
            break
    while len(answer) < k:
        answer.append(-1)
    return answer