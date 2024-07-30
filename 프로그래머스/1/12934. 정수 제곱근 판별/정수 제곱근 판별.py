def solution(n):
    x = int(n**(1/2))
    if n == int(x**2):
        return (x+1)**2
    else:
        return -1