# 31256 KB / 480 ms
import sys
input = sys.stdin.readline

n = int(input())
gom_x = set() # x좌표
gom_y = set() # y좌표

for i in range(n):
    line = input().rstrip()
    for j in range(n):
        if line[j] == 'G':
            gom_x.add(j)
            gom_y.add(i)

# G가 하나인 경우 움직일 필요 없음
if len(gom_x) == len(gom_y) == 1:
    print(0)
else:
    list_x = list(gom_x)
    list_x.sort()
    list_y = list(gom_y)
    list_y.sort()

    # x좌표나 y좌표가 하나뿐이면 모서리로 가지 않고 그냥 면으로 밀면 됨
    if len(gom_x) == 1:
        print(min(n-1-list_y[0], list_y[-1]))
    elif len(gom_y) == 1:
        print(min(n-1-list_x[0], list_x[-1]))
    # 이외에는 모서리로 밀어야 하므로 가로, 세로 최솟값 더해서 출력
    else:
        print(min(n-1-list_y[0], list_y[-1]) + min(n-1-list_x[0], list_x[-1]))