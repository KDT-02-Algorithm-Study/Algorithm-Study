import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
#          북       동      남       서
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0

while 1:
    # 현재 칸 0이면 청소
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    # 4방향 중 청소할 곳 있는지 확인
    is_be = False
    for dy, dx in delta:
        ny = r + dy
        nx = c + dx
        if 0 <= ny < n and 0 <= nx < m:
            if room[ny][nx] == 0:
                is_be = True

    # 청소할 곳이 있는 경우
    if is_be:
        for i in range(1, 5):
            # 반시계방향으로 돌며 가장 먼저 나오는 곳으로 인덱스 이동
            dy, dx = delta[(d+4-i)%4]
            if room[r+dy][c+dx] == 0:
                r = r + dy
                c = c + dx
                d = d + 4 - i
                break
    # 청소할 곳 없는 경우
    else:
        # 뒤가 벽이 아니면 이동, 벽이면 반목문 종료
        dy, dx = delta[(d+2)%4]
        if room[r+dy][c+dx] != 1:
            r = r + dy
            c = c + dx
        else:
            break

print(cnt)