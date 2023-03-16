# 10157 자리배정 https://www.acmicpc.net/problem/10157
# 65520KB / 736ms
import sys
input = sys.stdin.readline

c, r = map(int, input().split())
n = int(input())
check = [[0] * c for _ in range(r)]
# 좌석 번호 시작은 (0, 0)이 아니라 (0, r)
x = r
y = 0
# 시계 방향으로 돌기 위한 델타값
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
idx = 0

# 공연장 크기보다 대기번호가 크면 좌석을 가질 수 없으므로 print(0)
if n > c*r:
    print(0)
else:
    while True:
        # 대기번호 차례가 오면 해당 좌석 번호를 print
        if cnt == n:
            print(y+1, r-x)
            break
        
        # 좌석 번호가 공연장 번호를 벗어나면 방향을 바꿈
        if x+dx[idx] < 0 or y+dy[idx] < 0 or x+dx[idx] >= r or y+dy[idx] >= c:
            idx = (idx+1) % 4

        # 관객이 배정된 자리면 다시 방향을 바꿈
        if check[x+dx[idx]][y+dy[idx]] != 0:
            idx = (idx+1) % 4

        x += dx[idx]
        y += dy[idx]
        cnt += 1
        check[x][y] = cnt