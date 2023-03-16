# 10157 자리배정
# 37988 KB / 540 ms

c, r = map(int, input().split())
k = int(input())

# 자리보다 사람이 많으면 0출력 후 종료
if k > c*r:
    print(0)
    exit()

# 자리
g = [[False]*(c+1) for _ in range(r+1)]
# 상 우 하 좌
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
di = 0 # 진행 방향

# 현재 자리
sc = 1
sr = 1
g[1][1] = True

# 모든 자리 탐색
while k > 1:
    dc, dr = d[di]
    nc = sc + dc
    nr = sr + dr
    # 범위 밖으로 나가면 방향 바꿈
    if nc <= 0 or nc > c or nr <= 0 or nr > r:
        di = (di+1)%4
        continue
    # 자리가 비어있지 않으면 방향 바꿈
    if g[nr][nc]:
        di = (di+1)%4
        continue
    # 자리가 비어있으면 채우고 대기번호 마이너스
    g[nr][nc] = True
    k -= 1
    # 현재 자리 갱신
    sc, sr = nc, nr
print(sc, sr)