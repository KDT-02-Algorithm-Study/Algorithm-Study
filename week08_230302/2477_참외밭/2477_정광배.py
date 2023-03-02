# 2477 참외밭
# 31256 KB / 52 ms

import sys
input = sys.stdin.readline

k = int(input())    # 면적당 참외 수 입력

# 동 서 남 북
di = [1, -1, -1, 1]
#     1   2   3  4
#     x   x   y  y

x = y = 0       # 첫 시작은 (0, 0)
data = []       # 전체 꼭지점의 좌표 
xi = []         # x의 좌표
yi = []         # y의 좌표

for _ in range(6):
    d, l = map(int, input().split())    # 좌표 입력받기
    if d<3:     # x축 방향
        x += l*di[d-1]
        xi.append(x)
    else:       # y축 방향
        y += l*di[d-1]
        yi.append(y)
    data.append((x, y))     # 전체 꼭지점의 좌표

# x좌표, y좌표 정리
xi.sort()
yi.sort()
x_min = xi[0]
x_max = xi[2]
y_min = yi[0]
y_max = yi[2]

# 가장 큰 직사각형 넓이
area = (x_max-x_min)*(y_max-y_min)
# 가장 큰 직사각형에서 빼야할 직사각형 구하기
xyi = ((x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max))
for i in xyi:
    if i not in data:
        ex = (i[0]-xi[1])*(i[1]-yi[1])
        
result = (area - abs(ex)) * k
print(result)