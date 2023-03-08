import sys
sys.setrecursionlimit(10**6)

def z(n, y, x):
    global cnt
    l = 2 ** (n-1)

    if y < l:
        if x < l:
            pass
        else:
            cnt += l ** 2
            x -= l
    else:
        if x < l:
            cnt += l ** 2 * 2
            y -= l
        else:
            cnt += l ** 2 * 3
            y -= l
            x -= l

    if n == 1:
        return
    else:
        z(n-1, y, x)
    
n, r, c = map(int, sys.stdin.readline().split())
cnt = 0
z(n, r, c)
print(cnt)