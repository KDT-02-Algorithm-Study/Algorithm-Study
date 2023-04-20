# 5212 지구 온난화
# 31704 KB / 60 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
import copy

r,c = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]
new_graph = copy.deepcopy(graph)
visited = [[False]*c for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ground_x,ground_y = [],[]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            cnt = 0 
            ground_x.append(i)
            ground_y.append(j)
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= r or ny < 0 or ny >= c :
                    cnt += 1
                elif 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                        cnt += 1
            if cnt >=3 :
                new_graph[i][j] = '.'
                ground_x.pop()
                ground_y.pop()
x_max,x_min = max(ground_x),min(ground_x)
y_max,y_min = max(ground_y),min(ground_y)

for x in range(x_min,x_max+1):
    for y in range(y_min,y_max+1):
        print(new_graph[x][y], end = '')
    print(sep = '\n')




    
