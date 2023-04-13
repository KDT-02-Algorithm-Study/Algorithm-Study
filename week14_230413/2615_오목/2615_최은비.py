# 오목 https://www.acmicpc.net/problem/2615
# 31256KB / 40ms
import sys
input = sys.stdin.readline

def check(x, y):
    global end
    color = board[x][y]

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        cnt = 0

        while 0 <= nx < 19 and 0 <= ny < 19:
            if board[nx][ny] != color:
                break
                
            cnt += 1            
            if cnt == 4:
                if 0 <= x - dx < 19 and 0 <= y - dy < 19 and board[x - dx][y - dy] == color:
                    break
                if 0 <= nx + dx < 19 and 0 <= ny + dy < 19 and board[nx + dx][ny + dy] == color:
                    break
                
                print(color)
                print(x+1, y+1)

                end = True
                break

            nx += dx
            ny += dy

        if end:
            break
    
    return end

board = [0 for _ in range(19)]
dxy = [(1, 0), (0, 1), (1, 1), (-1, 1)]
end = False

for i in range(19):
    board[i] = list(map(int, input().split()))

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            check(i, j)
        
        if end:
            break

    if end:
        break

if not end:
    print(0)
