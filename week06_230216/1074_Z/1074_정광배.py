# 1074 Z

import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_(n, x, y):
    # 종료 조건
    if n == 1:
        return 0
    
    g = n//2 # 다음 분할 간격
    nx = x + g
    ny = y + g

    # 분할
    if r < nx and c < ny:       # 좌상
        return find_(g, x, y)
    elif r < nx and c >= ny:    # 우상
        return find_(g, x, ny) + g**2
    elif r >= nx and c < ny:    # 좌하
        return find_(g, nx, y) + (g**2)*2
    elif r >= nx and c >= ny:   # 우하
        return find_(g, nx, ny) + (g**2)*3

N, r, c = map(int, input().split())
print(find_(2**N, 0, 0)) # 인자를 2**N으로