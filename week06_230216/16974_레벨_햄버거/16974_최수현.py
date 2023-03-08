import sys

def burger(n, x, patty):
    if n == 1:
        s = 'BPPPB'
        patty += s[:x].count('P')
        return patty
    
    l = 2**(n+2) - 3
    p = 2**(n+1) - 1

    if x == l:
        return patty + p
    elif x > p:
        patty += p//2 + 1
        return burger(n-1, x-p, patty)
    elif x == p:
        return patty + (p//2 + 1)
    elif x > 1:
        return burger(n-1, x-1, patty)
    else:
        return patty

N, X = map(int, input().split())
print(burger(N, X, 0))