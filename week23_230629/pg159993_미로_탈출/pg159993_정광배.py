# 미로 탈출
# 테스트 17 〉	통과 (11.68ms, 10.4MB)

from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(start:tuple, end:str, maps:list, r:int, c:int):
    visited = [[False]*c for _ in range(r)]
    q = deque([start])

    while q:
        x, y, d = q.popleft()
        if maps[x][y] == end:
            return d
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0<= nx <r and 0<= ny <c and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    q.append((nx, ny, d+1))
                    visited[nx][ny] = True
    return 0


def solution(maps):
    r = len(maps)
    c = len(maps[0])

    # S와 L 좌표 찾기
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'S':
                s = (i, j, 0)
            if maps[i][j] == 'L':
                l = (i, j, 0)

    s_l = bfs(s, 'L', maps, r, c)	# 시작 -> 레버
    l_e = bfs(l, 'E', maps, r, c)   # 레버 -> 출구

    if s_l and l_e: # 레버와 출구 까지 길이 있을 경우
        answer = s_l + l_e
    else:
        answer = -1
    return answer