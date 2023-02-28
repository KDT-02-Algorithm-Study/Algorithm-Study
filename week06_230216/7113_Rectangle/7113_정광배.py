# 7113 Rectangle

import sys
sys.setrecursionlimit(10**6)

def cut(n, m, c):
    # 큰 수 - 작은 수
    if n < m:
        return cut(n, m-n, c+1)
    elif n > m:
        return cut(n-m, m, c+1)
    else:   # 종료 조건
        return c+1 # 개수는 자른 횟수 + 1

n, m = map(int, input().split())
print(cut(n, m, 0))