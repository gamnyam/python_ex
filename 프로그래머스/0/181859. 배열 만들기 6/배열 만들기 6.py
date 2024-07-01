def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        if stk and stk[-1]==arr[i]:
            stk.pop()
        elif stk and stk[-1]!=arr[i]:
            stk.append(arr[i])
        else:
            stk.append(arr[i])
    return stk or [-1]