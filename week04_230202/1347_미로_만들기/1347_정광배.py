# 1347 미로 만들기

n = int(input())
data = input()

# 지도 초기화
graph = [['#']*101 for _ in range(101)]
x=50
y=50
graph[x][y] = '.'

# 남 서 북 동(우회전)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# 보고있는 방향
direct = 0

x_max = y_max = x
x_min = y_min = y

for i in data:
    if i == 'F':
        # 보고있는 방향으로 이동
        x += dx[direct]
        y += dy[direct]
        graph[x][y] = '.'

        x_max = max(x_max, x)
        y_max = max(y_max, y)
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        
    elif i == 'R': # 우회전
        direct = (direct+1)%4

    elif i == 'L': # 좌회전
        direct = (direct-1)%4

# 범위 출력
for x1 in range(x_min, x_max + 1):
    for y1 in range(y_min, y_max + 1):
        print(graph[x1][y1],end='')
    print()