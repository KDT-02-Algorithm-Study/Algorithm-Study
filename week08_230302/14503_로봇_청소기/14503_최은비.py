# 로봇청소기 https://www.acmicpc.net/problem/14503
# 31256KB, 44ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [0] * n
# 북동남서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    room[i] = list(map(int, input().split()))

room[x][y] = -1 # 청소했다는 표시
cnt = 1 # 무조건 청소를 한 번 하고 시작하므로 1로 초기화

while True:
    dirty = False # 주변에 청소된 칸이 있는지 없는지 판단할 변수

    # 주위 4칸 탐색
    for _ in range(4):
        d = (d+3) % 4 # 청소기 방향은 북-동-남-서지만 반시계 방향으로 탐색하려면 북-서-남-동이여야 함
        nx = x + dx[d]
        ny = y + dy[d]

        # 주위 4칸 중에 청소 안 한 칸이 있으면 그 칸을 청소하고 다시 탐색
        if 0 < nx <= n and 0 < ny <= m and room[nx][ny] == 0:
            room[nx][ny] = -1
            cnt += 1 
            x = nx
            y = ny
            dirty = True
            break
    
    # 청소 안 한 칸이 없으면
    if not dirty:
        # 현재 방향으로 후진했을 때 벽인 경우 종료
        if room[x - dx[d]][y - dy[d]] == 1:
            print(cnt)
            break
        # 벽이 아니면 후진하기
        else:
            x -= dx[d]
            y -= dy[d]
