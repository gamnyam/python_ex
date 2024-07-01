def solution(picture, k):
    answer = []
    for row in picture:
        exi = ''
        for char in row:
            exi += char*k
        for _ in range(k):
            answer.append(exi)
    return answer