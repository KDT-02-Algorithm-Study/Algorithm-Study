# 16918 봄버맨
# 31256 KB / 96 ms

import sys
input = sys.stdin.readline

# 우 하 좌 상
dxy = ((0, 1),(1, 0),(0,-1),(-1, 0))

r, c, n = map(int, input().split())
g0 = [input().rstrip() for _ in range(r)] # 초기 상태, 1초
# g2 = [['O']*c for _ in range(r)] # n이 짝수일 때
g3 = [['O']*c for _ in range(r)] # n%4 == 3 일 때
g1 = [['O']*c for _ in range(r)] # n%4 == 1 일 때

# g0에서 g3갈 때
for x in range(r):
    for y in range(c):
        if g0[x][y] == 'O':
            g3[x][y] = '.'
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                g3[nx][ny] = '.'
# g3에서 g1갈 때
for x in range(r):
    for y in range(c):
        if g3[x][y] == 'O':
            g1[x][y] = '.'
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                g1[nx][ny] = '.'

# 출력 분기 처리
if n == 1:
    print('\n'.join(g0))
elif n%4 == 1:
    for g in g1:
        print(''.join(g))
elif n%4 == 3:
    for g in g3:
        print(''.join(g))
else: # 짝수일 때
    [print('O'*c) for _ in range(r)]
    # for g in g2:
    #     print(''.join(g))