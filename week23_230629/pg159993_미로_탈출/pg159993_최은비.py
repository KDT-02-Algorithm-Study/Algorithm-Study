# 프로그래머스 미로 탈출
# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 출발점 -> 레버 까지의 최단거리 + 레버 -> 도착점 까지의 최단거리

from collections import deque

def start_to_lever(maps, x, y):
    r = len(maps)
    c = len(maps[0])
    lever = False
    visited = [[0 for _ in range(c)] for _ in range(r)]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    que = deque()
    que.append((x, y, 0))
    visited[x][y] = 0
    
    while que:
        x, y, cnt = que.popleft()
        
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = cnt + 1
                if maps[nx][ny] == 'L':
                    lever = True
                    break
                else:
                    que.append((nx, ny, visited[nx][ny]))
        
        if lever:
            break

    return (lever, visited[nx][ny])

    
def lever_to_end(maps, x, y):
    r = len(maps)
    c = len(maps[0])
    end = False
    visited = [[0 for _ in range(c)] for _ in range(r)]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    que = deque()
    que.append((x, y, 0))
    visited[x][y] = 0
    
    while que:
        x, y, cnt = que.popleft()
        
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = cnt + 1
                if maps[nx][ny] == 'E':
                    end = True
                    break
                else:
                    que.append((nx, ny, visited[nx][ny]))
        
        if end:
            break

    return (end, visited[nx][ny])
    

def solution(maps):
    answer = -1
    r = len(maps)
    c = len(maps[0])
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'S':
                lever, stl_cnt = start_to_lever(maps, i, j)
                break
            
    if lever:
        for i in range(r):
            for j in range(c):
                if maps[i][j] == 'L':
                    end, lte_cnt = lever_to_end(maps, i, j)
                    break
                    
    if lever and end:
        answer = stl_cnt + lte_cnt

    return answer