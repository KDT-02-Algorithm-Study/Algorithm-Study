# https://www.acmicpc.net/problem/1347

import sys
input = sys.stdin.readline

n = int(input())
route = input().strip()

# 현재 위치
x = y = 0
# 이동할 수 있는 좌표를 저장할 리스트
tmp = [[0, 0]]
# 회전했을 때 방향을 바꿔주기 위한 리스트
# 남 -> 서 -> 북 -> 동 방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
now = 0

for char in route:
    if char == "R":
        now += 1
    elif char == "L":
        now += 3
    else:
        # 회전했을 때 실제로 이동한 좌표를 tmp 리스트에 저장
        x += dx[now % 4]
        y += dy[now % 4]
        tmp.append([x, y])

# 최종 미로의 길이를 정해주기 위한 각 좌표들의 최소, 최대값
x_min = min(tmp)[0]
y_min = min(tmp, key=lambda x: x[1])[1]

x_max = max(tmp)[0]
y_max = max(tmp, key=lambda x: x[1])[1]

# 음수가 있을 경우 그 값을 기준으로 0을 만들어주기 위해 모든 값에 최소값의 절대값을 더해줌
for val in tmp:
    val[0] += abs(x_min)
    val[1] += abs(y_min)

# 미로의 크기는 각 좌표의 최대값-최소값에 1일 더한 값
maze = [[0 for _ in range(y_max-y_min+1)] for _ in range(x_max-x_min+1)]

# tmp에 저장된 좌표는 이동할 수 있는 좌표이므로 .으로 바꿔주기
for val in tmp:
    maze[val[0]][val[1]] = "."

# maze를 순회하면서 갈 수 없는 곳(값이 0인 인덱스)은 #으로 바꿔주고 출력
for i in range(x_max-x_min+1):
    for j in range(y_max-y_min+1):
        if maze[i][j] == 0:
            print("#", end ="")
        else:
            print(maze[i][j], end="")

    print()
