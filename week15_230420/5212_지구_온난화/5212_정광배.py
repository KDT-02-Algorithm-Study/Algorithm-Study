# 5212 지구 온난화
# 31256 KB / 40 ms

import sys
input = sys.stdin.readline

r, c = map(int, input().split()) # 행 열
g = [input().rstrip() for _ in range(r)] # graph

# 우 하 좌 상
dxy = ((0, 1),(1, 0),(0, -1),(-1, 0))

new = [['.']*c for _ in range(r)] # new

# 완전 탐색
for i in range(r):
    for j in range(c):
        if g[i][j] == 'X':
            cnt = 0 # 바다 cnt
            # 델타 탐색
            for dx, dy in dxy:
                nx = i + dx
                ny = j + dy
                # 지도 밖
                if nx < 0:
                    cnt += 1
                elif nx >= r:
                    cnt += 1
                if ny < 0:
                    cnt += 1
                elif ny >= c:
                    cnt += 1
                # 바다
                if 0 <= nx < r and 0 <= ny < c:
                    if g[nx][ny] == '.':
                        cnt += 1
            # '.'부터 시작했으므로
            if cnt <= 2:
                new[i][j] = 'X'

# 줄에 'X'존재여부 탐색은 못쓴다.
# strip('.')은 못쓴다. 
# 인덱스로 탐색
r_start , c_start = r, c
r_end = c_end = 0
# 행 탐색
for row in new:
    if 'X' in row:
        c_start = min(c_start, row.index('X'))
        c_end = max(c_end, c - row[::-1].index('X'))

# 열 탐색
temp = list(zip(*new))
for col in temp:
    if 'X' in col:
        r_start = min(r_start, col.index('X'))
        r_end = max(r_end, r - col[::-1].index('X'))

# 출력
for i in range(r_start,r_end):
    print(''.join(new[i][c_start:c_end]))

# for row in new[r_start:r_end]: # 슬라이스로 접근(더 느림)
#     print(''.join(row[c_start:c_end]))