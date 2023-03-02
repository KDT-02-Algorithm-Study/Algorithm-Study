dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def cleaning(x, y, d):
    global clean
    if room[x][y] == 0:
        room[x][y] = 2
        clean += 1
    for _ in range(4):
        nd = (d+3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if room[nx][ny] == 0:
            cleaning(nx, ny, nd)
            return
        d = nd
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if room[nx][ny] == 1:
        return
    cleaning(nx, ny, d)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [[int(x) for x in input().split()] for _ in range(N)]
clean = 0

cleaning(r, c, d)
print(clean)