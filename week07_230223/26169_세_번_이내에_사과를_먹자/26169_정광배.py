# 26169 세 번 이내에 사과를 먹자
# 31712KB 72ms 818B

import sys
sys.stdin = open('input.txt', 'r')

import sys, copy
input = sys.stdin.readline

def dfs(x, y, t, a, v):
    v = [[False]*5 for _ in range(5)]
    v[x][y] = True
    s = [(x, y, t, a, v)]
    while s:
        x, y, t, a, v = s.pop()
        if g[x][y] == 1:
            a += 1
            if a == 2:
                return 1
        if t == 3:
            continue
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if not v[nx][ny] and g[nx][ny] != -1:
                v[nx][ny] = True
                v1 = copy.deepcopy(v)
                s.append((nx, ny, t+1, a,v1))
    return 0

g = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(dfs(r, c, 0, 0, 0))