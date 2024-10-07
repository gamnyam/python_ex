
def solution(numbers, target):
    visited = [False] * len(numbers)
    answer = []
    
    def dfs(node, total):
        
        if node == len(numbers):
            if total == target:
                answer.append(total)
            return

        number = numbers[node]


        dfs(node + 1, total + number)
        dfs(node + 1, total - number) 


    dfs(0, 0)
        
    return len(answer)