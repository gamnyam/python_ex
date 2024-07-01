def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            while len(arr)>len(arr[i]):
                arr[i].append(0)
                if len(arr) == len(arr[i]):
                    break
            while len(arr)<len(arr[i]):
                arr.append([0]*len(arr[i]))
                if len(arr) ==len(arr[i]):
                    break
                
    return arr