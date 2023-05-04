# https://www.acmicpc.net/problem/21610
# 21610 마법사 상어와 비바라기
# 31256KB / 436ms
import sys
sys.stdin = open("input_21610.txt", "r")

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
moves = []
for i in range(M):
    tmp = list(map(int,input().split()))
    moves.append([tmp[0]-1,tmp[1]])



# 처음 클라우드 생성
cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]

# 방향 설정
dx8 = [0, -1, -1, -1, 0, 1, 1, 1] 
dy8 = [-1, -1, 0, 1, 1, 1, 0, -1]  

# 4번의 이동을 할 것임, 모든 구름이 이동
for i in range(M):
    # step 1 
    # 이동
    move = moves[i]
    next_clouds = []

    # 모든 클라우드에 대해서 이동을 설정

    for c in cloud:
        # 현재 조건
        x = c[0]
        y = c[1]
        d = move[0] # 어떤 방향으로
        s = move[1] # 몇 번 이동

        # 다음 조건
        nx = (x + dx8[d]*s)%N
        ny = (y + dy8[d]*s)%N
        next_clouds.append([nx,ny])

    # step 2
    # 방문처리에 대한 값
    # 이동한 부분에 대해서 저장된 물의 양 1 증가
    visited = [[False]*N for _ in range(N)]
    for c in next_clouds:
        x = c[0]
        y = c[1]
        graph[x][y] +=1
        visited[x][y] = True


    # step 3
    cloud = []

    # step 4
    # 물복사버그 마법을 시전
    # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수 만큼
    # 바구니의 물의 양이 증가 (경계 넘어가는 곳은 고려 안 함) 
    dx4 = [-1,-1,1,1]
    dy4 = [-1,1,-1,1]

    for c in next_clouds:
        x = c[0]
        y = c[1]
        cnt = 0 
        for j in range(4):
            nx = x + dx4[j]
            ny = y + dy4[j]

            # 범위를 넘어가면 안되고, 1이상의 물이 있는 경우에만 물을 하나씩 끌어다옴
            if (0 <= nx < N) and (0 <=ny < N) and (graph[nx][ny]>= 1):
                cnt += 1

        graph[x][y] += cnt

    
    # step 5
    for k in range(N):
        for o in range(N):
            if (graph[k][o]>=2) and (visited[k][o] == False) :
                graph[k][o]-=2
                cloud.append([k,o])

ans = 0 
for i in range(N):
    ans += sum(graph[i])
print(ans)
            









