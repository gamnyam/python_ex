def solution(arr, queries):
    answer = arr
    for i, j in queries:
        arr[i],arr[j] = arr[j],arr[i]
        answer = arr
    return answer