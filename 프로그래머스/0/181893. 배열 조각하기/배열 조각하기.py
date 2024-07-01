def solution(arr, query):
    answer = arr
    for q in range(len(query)):
        if q % 2==0:
            arr=arr[:query[q]+1]
        else :
            arr=arr[query[q]:]
    return arr