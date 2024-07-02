def solution(n):
    array = [[0]*n for _ in range(n)]
    count = 1
    sr = 0
    er = n-1
    sc = 0
    ec = n-1

    while count <=n*n :
        for i in range(sc, ec+1):
            array[sr][i] = count
            count += 1
        sr +=1

        for i in range(sr, ec+1):
            array[i][ec] = count
            count +=1
        ec -= 1

        for i in range(ec, sc -1, -1):
            array[er][i] = count
            count +=1
        er -=1

        for i in range(er, sr-1, -1):
            array[i][sc] = count
            count +=1
        sc +=1

    return array