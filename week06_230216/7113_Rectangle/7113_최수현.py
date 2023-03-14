import sys
sys.setrecursionlimit(10**6)

def rec(x, y, cnt):
    cnt += 1
    if x == y:
        return cnt
    if x > y:
        cnt = rec(x-y, y, cnt)
    else:
        cnt = rec(y-x, x, cnt)
    
    return cnt

n, m = map(int, input().split())
print(rec(n, m, 0))