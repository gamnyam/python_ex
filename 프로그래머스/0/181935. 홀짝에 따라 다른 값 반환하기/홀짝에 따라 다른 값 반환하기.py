def solution(n):
    ans = 0
    if n%2 == 0 :
        for i in range(n+1) :
            if i%2 == 0 :
                ans += i**2
    else :
        for i in range(n+1) :
            if i%2 != 0 :
                ans += i
    return ans

# 참고 답안
def solution(n):
    answer = 0  # 결과값을 저장할 변수 초기화
    if n % 2:   # n을 2로 나눈 나머지가 1인지 확인 (n이 홀수인지 확인)
        for i in range(1, n+1, 2):  # 1부터 n까지 2씩 증가하면서 (홀수만)
            answer += i  # 홀수 i를 answer에 더함
    else:  # n이 짝수인 경우
        for i in range(2, n+1, 2):  # 2부터 n까지 2씩 증가하면서 (짝수만)
            answer += i**2  # 짝수 i의 제곱을 answer에 더함
    return answer 
