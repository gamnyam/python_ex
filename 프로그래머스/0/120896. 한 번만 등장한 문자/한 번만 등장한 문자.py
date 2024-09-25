from collections import defaultdict
def solution(s):
    answer = ''
    dic = defaultdict(int)
    
    for char in s:
        dic[char] = dic[char] + 1
    
    # value가 1인 key 탐색
    
    for key in dic :
        # key : 문자, value : 문자의 개수
        value = dic[key]
        
        if value == 1 :
            answer += key
            
    # 문자열 정렬 sorted() 활용
    # sorted(컨테이너 자료형)는정렬된 리스트를 반환 
    answer = sorted(answer) 
    answer = "".join(answer)
    
    return answer