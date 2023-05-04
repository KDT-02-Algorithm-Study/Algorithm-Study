# 21610 л§ҲлІ•мӮ¬ мғҒм–ҙмҷҖ л№„л°”лқјкё° # 이거 뭐임;;
# 117272 KB / 500 ms pypy3 ㅠㅠ

import sys
input = sys.stdin.readline

# 0+ 좌 좌상 상 우상 우 우하 하 좌하
dxy = (0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

c = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    # 이동
    move_ = []
    d, s = map(int, input().split())
    for x, y in c:
        nx, ny = (x + dxy[d][0]*s)%n, (y + dxy[d][1]*s)%n
        g[nx][ny] += 1
        move_.append((nx, ny))
    
    # 물 복사
    for x, y in move_:
        cnt = 0
        for dx, dy in dxy[2::2]: # 대각
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif g[nx][ny] > 0:
                cnt += 1
        g[x][y] += cnt
    
    # 구름 생성
    new_ = []
    for x in range(n):
        for y in range(n):
            if (x, y) in move_ or g[x][y] < 2:
                continue
            g[x][y] -= 2
            new_.append((x, y))
    c = new_
r = 0
for x in range(n):
    for y in range(n):
        r += g[x][y]
print(r)