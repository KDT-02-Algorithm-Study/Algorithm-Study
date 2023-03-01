# 14503 로봇 청소기
# 31256 KB / 44 ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# 문자열로 데이터 입력 받기
data = [input().rstrip().replace(' ','') for _ in range(n)] # 0빈칸 1벽
visited = [[False]*m for _ in range(n)]

# 북 동 남 서
di = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0
ans = 0
while True:
    # 청소 안 했으면 청소
    if not visited[r][c]:   
        visited[r][c] = True
        ans += 1

    # 4방향 모두 확인했을 때
    if cnt == 4:
        # 후진
        nr = r - di[d][0]
        nc = c - di[d][1]
        # 밖으로 나갈 경우(는 없는데 이걸 빼면 시간이 52ms가 나온다..)
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            break
        # 벽일 경우
        if data[nr][nc] == '1':
            break
        # 후진 성공
        r = nr
        c = nc
        cnt = 0

    d = (d+3)%4 # 좌회전

    nr = r + di[d][0]
    nc = c + di[d][1]

    # 바라보고 있는 방향 검사
    # 마찬가지..
    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        cnt += 1
        continue
    # 벽이거나 청소한 경우
    if data[nr][nc] == '1' or visited[nr][nc]:
        cnt += 1
        continue

    # 전진 성공
    r = nr
    c = nc
    cnt = 0

print(ans)






    # if 0 < nr <= n and 0 < nc <= m:
    #     if 

    


    # for dr, dc in di:
    #     nr = r + dr
    #     nc = c + dc
    #     if nr < 0 or nr >= n or nc < 0 or nc >= m:
    #         continue
    #     if data[nr][nc] == '0' and not visited[nr][nc]:
    #         flag = True
    #         break
    # if flag:
    #     d = (d+3)//4
    #     nr = r + di[d][0]
    #     nc = c + di[d][1]
    #     if data[nr][nc] == '0' and not visited[nr][nc]:
    #         r = nr
    #         c = nc

    # if nr < 0 or nr >= n or nc < 0 or nc >= m or visited[nr][nc] or data[nr][nc]:
    #     d = (d+3)//4
    #     cnt += 1
    #     continue
