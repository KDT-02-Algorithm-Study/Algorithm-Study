# 경비원 https://www.acmicpc.net/problem/2564
# 31256KB / 44ms
import sys
input = sys.stdin.readline

# 가로, 세로
r, c = map(int, input().split())
n = int(input())
# 1: 북 2: 남 3: 서 4: 동
# 북남 - 왼쪽부터의 거리, 동서 - 위쪽부터의 거리
direction = []
distance = []

for _ in range(n):
    a, b = map(int, input().split())
    direction.append(a)
    distance.append(b)

dg_dir, dg_dis = map(int, input().split())
# direction = [1, 3, 2]
# distance = [4, 2, 8]

ans = 0
for i in range(n):
    # 같은 방향에 있는 경우
    if direction[i] == dg_dir:
        # 거리끼리 뺀 값이 최소
        ans += abs(distance[i] - dg_dis)
    # 반대 방향에 있는 경우
    # 북+남 = 3 / 동+서 = 7
    elif (direction[i] + dg_dir) == 3 or (direction[i] + dg_dir) == 7:
        # 북+남
        if dg_dir == 1 or dg_dir == 2:
            # 시계 방향과 반시계 방향 중에서 최소값 구하기
            ans += c + min(dg_dis + distance[i], r - dg_dis + r - distance[i])
        # 동+서
        else:
            ans += r + min(dg_dis + distance[i], c - dg_dis + c - distance[i])
    else:
        # 동근이가 북쪽일 때
        if dg_dir == 1:
            # 상점이 서쪽
            if direction[i] == 3:
                ans += dg_dis + distance[i]
            # 상점이 동쪽
            else:
                ans += r - dg_dis + distance[i]
        # 동근이가 남쪽일 때
        elif dg_dir == 2:
            if direction[i] == 3:
                ans += dg_dis + c - distance[i]
            else:
                ans += r - dg_dis + c - distance[i]
        # 동근이가 서쪽일 때
        elif dg_dir == 3:
            # 상점이 북쪽
            if direction[i] == 1:
                ans += dg_dis + distance[i]
            # 상점이 남쪽
            else:
                ans += c - dg_dis + distance[i]
        # 동근이가 동쪽일 때
        else:
            if direction[i] == 1:
                ans += dg_dis + r - distance[i]
            else:
                ans += c - dg_dis + r - distance[i]
                
print(ans)