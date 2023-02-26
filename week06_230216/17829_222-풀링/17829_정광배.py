# 17829 222-풀링

import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def p(n, x, y):
    # 종료 조건
    if n == 2:
        tmp = data[x][y:y+2] + data[x+1][y:y+2]
        tmp.sort()
        return tmp[-2]
    
    # 재귀
    g = n//2
    tmp = [
        p(g, x, y),
        p(g, x+g, y),
        p(g, x, y+g),
        p(g, x+g, y+g)
    ]
    tmp.sort()
    return tmp[-2]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

print(p(N, 0, 0))