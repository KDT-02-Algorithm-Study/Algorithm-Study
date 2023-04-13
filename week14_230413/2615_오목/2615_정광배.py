# 2615 오목
# 31256 KB / 44 ms

import sys
input = sys.stdin.readline

def omok(x, y):
    # 방향마다 검사
    for dx, dy in dxy:
        # 뒷칸 검사
        bx = x - dx
        by = y - dy
        # 뒷칸이 target이면 건너뛰기
        if bx >= 0 and by >= 0 and bx < 19:
            if g[bx][by] == target:
                continue
        
        # 진행방향 탐색
        cnt = 0
        for i in range(1, 5):
            nx = x + dx*i
            ny = y + dy*i
            if nx >= 19 or ny >= 19 or nx < 0:
                break
            if g[nx][ny] != target:
                break
            else:
                cnt += 1
            
            # 육목 확인
            if cnt == 4:
                nx += dx
                ny += dy
                # 끝자리이거나 5목일 경우 True
                if nx < 0 or nx >= 19 or ny >= 19 or g[nx][ny] != target:
                    return True
    return False

# 우 하 우상 우하
dxy = ((0, 1), (1, 0), (-1, 1), (1, 1))

g = [input().split() for _ in range(19)]
flag = 0

# 탐색
for i in range(19):
    for j in range(19):
        if not g[i][j] == '0':
            target = g[i][j]
            if omok(i, j):
                flag = 1
                break
    if flag:
        break
    
if flag:
    print(target)
    print(i+1, j+1)
else:
    print(0)
