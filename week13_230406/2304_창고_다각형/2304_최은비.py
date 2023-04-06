# 창고 다각형 https://www.acmicpc.net/problem/2304
# 31256KB / 48ms
import sys
input = sys.stdin.readline

n = int(input())
col = []
max_ = 0
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    col.append((a, b))

# 왼쪽 면 위치를 기준으로 정렬
col = sorted(col)

# 가장 높은 기둥의 인덱스 찾기
for i in range(n):
    if max(col, key=lambda x: x[1])[1] == col[i][1]:
        max_ = i
        break

# 가장 높은 기둥 인덱스를 기준으로 왼쪽과 오른쪽으로 나눠서 계산

# max 기둥의 왼쪽은 현재 기둥보다 높은 기둥을 만나기 전까지 같은 높이를 더해줌
tmp = col[0][1]
for i in range(max_):
    # 기둥 높이에 왼쪽 면 위치 차이를 곱해서 더해주기
    ans += tmp * (col[i+1][0] - col[i][0])

    # 현재 기둥보다 다음 기둥이 높으면 기준을 갱신
    if tmp < col[i+1][1]:
        tmp = col[i+1][1]

# max 기둥의 오른쪽도 동일하게 계산
tmp = col[-1][1]
for i in range(n-1, max_, -1):
    ans += tmp * (col[i][0] - col[i-1][0])

    if tmp < col[i-1][1]:
        tmp = col[i-1][1]

print(ans + col[max_][1])

