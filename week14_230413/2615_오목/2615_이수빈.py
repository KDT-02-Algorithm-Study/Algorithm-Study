# 2615 오목
# 31256 KB / 44 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

graph = []
for i in range(19):
    graph.append(list(map(int, input().split())))

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if graph[x][y] != 0:
            doll = graph[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == doll:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and graph[x - dx[i]][y - dy[i]] == doll:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and graph[nx + dx[i]][ny + dy[i]] == doll:
                            break
                        print(doll)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)


'''
graph = [list(map(int,input().split())) for _ in range(19)]

# 좌 & 우, 상 & 하, 우대각선, 좌대각선

dx = [0,1,1,1]
dy = [1,0,1,-1]

def dfs(x,y,d,k):

    if x < 0 or x >= 19 or y < 0 or y >= 19 :
        return False

    if visited[x][y] == False and graph[x][y] == d : 
        doll_list.append([d,x,y])
        visited[x][y] = True
        nx = x + dx[k]
        ny = y + dy[k]
        dfs(nx,ny,d,k)
        return True
    return False

black,white = [],[]

for d in range(1,3):
    for j in range(19):
        for i in range(19):
            for k in range(4):
                visited = [[False]*19 for _ in range(19)] 
                doll_list = []
                if dfs(i,j,d,k) == True:
                    if len(doll_list) == 5 :
                        # 육목 확인
                        if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and graph[i - dx[k]][j - dy[k]] != d \
                            and 0 <= i + dx[k] < 19 and 0 <= j + dy[k] < 19 and graph[i + dx[k]][j + dy[k]] != d:
                            if d == 1 :
                                black.append(doll_list)
                            elif d == 2 :
                                white.append(doll_list)
if len(black)>len(white):
    black = sorted(black[0], key = lambda x : (x[2],x[1]))
    print(1)
    print(black[0][1]+1,black[0][2]+1)
elif len(black)<len(white):
    white = sorted(white[0], key = lambda x : (x[2],x[1]))
    print(2)
    print(white[0][1]+1,white[0][2]+1)
elif len(black) == len(white):
    print(0)

'''