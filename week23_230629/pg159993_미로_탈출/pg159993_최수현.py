from collections import deque

# 시작점과 목표 지점 bfs 탐색
def bfs(start, maze=list, target=str):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    check = [[False]*len(maze[0]) for _ in range(len(maze))]
    q = deque([(start[0], start[1], 0)])
    check[start[0]][start[1]] = True

    while q:
        y, x, turn = q.popleft()
        if maze[y][x] == target:
            return turn
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and not check[ny][nx] and maze[ny][nx] != 'X':
                check[ny][nx] = True
                q.append((ny, nx, turn+1))
    else:
        return -1


def solution(maps):
    s = (0, 0)
    l = (0, 0)
    # S와 L의 좌표값 구하기
    for i, line in enumerate(maps):
        if 'S' in line:
            s = (i, line.index('S'))
            break
    for i, line in enumerate(maps):
        if 'L' in line:
            l = (i, line.index('L'))
            break
    
    step1 = bfs(s, maps, 'L')
    if step1 == -1:
        return -1
    
    step2 = bfs(l, maps, 'E')
    if step2 == -1:
        return -1

    return step1 + step2