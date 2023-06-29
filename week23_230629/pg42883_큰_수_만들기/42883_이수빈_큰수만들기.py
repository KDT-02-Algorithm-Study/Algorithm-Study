
# 159993 미로탈출
# 0.04ms, 10.3MB
# 11.04ms, 10.2MB
from collections import deque

def find_point(maps):
    col,row = len(maps),len(maps[0])
    for c in range(col):
        for r in range(row):
            if maps[c][r] == 'S':
                s = (r,c)
            elif maps[c][r] == 'L':
                l = (r,c)
    
    return s,l

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(maps,start,end):
    x,y = start
    col, row = len(maps), len(maps[0])
    visited = [[False]*row for _ in range(col)]
    visited[y][x] = True
    
    queue = deque()
    queue.append([x,y,0])

    while queue : 
        x,y,dist = queue.popleft()
        if maps[y][x] == end :
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < row and -1 < ny < col and not visited[ny][nx] and maps[ny][nx] != 'X' :
                visited[ny][nx] = True
                queue.append((nx,ny,dist+1))
    return -1

def solution(maps):    
    s, l = find_point(maps)
    lever_dist = bfs(maps,s, 'L')
    end_dist = bfs(maps,l, 'E')
    
    return lever_dist + end_dist if lever_dist > -1 and end_dist > -1 else -1
