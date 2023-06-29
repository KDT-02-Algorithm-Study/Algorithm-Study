from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    
    def dfs(_from, _to):
        visited = [[0] * col for _ in range(row)]
        queue = deque()
        queue.append(_from)
        visited[_from[0]][_from[1]] = 1
        
        while queue:
            x, y = queue.popleft()
            
            if x == _to[0] and y == _to[1]:
                return visited[x][y] - 1
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return 0
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                start = (i, j)
            if maps[i][j] == 'E':
                exit = (i, j)
            if maps[i][j] == 'L':
                lever = (i, j)

    start_to_lever = dfs(start, lever)
    lever_to_exit = dfs(lever, exit)
    
    
    if start_to_lever and lever_to_exit:
        answer = start_to_lever + lever_to_exit
        return answer
    else:
        return -1