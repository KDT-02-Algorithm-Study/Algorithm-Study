# 31256 KB / 44 ms

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
graph = [[int(x) for x in input().split()] for _ in range(19)]

def check(x, y, num):
    for d in range(4):
        cnt = 1
        nx = x + dx[d]
        ny = y + dy[d]
        # 다음 수가 범위 안에 있고, 같은 수 일때
        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == num:
            cnt += 1
            # 오목일 때 육목을 걸러냄 (양쪽 끝을 검사)
            if cnt == 5:
                # 이전 수도 같으면 육목이니 제외
                if 0 <= x - dx[d] < 19 and 0 <= y - dy[d] < 19 and graph[x - dx[d]][y - dy[d]] == num:
                    break
                # 다음 수도 같으면 육목이니 제외
                if 0 <= (nx + dx[d]) < 19 and 0 <= (ny + dy[d]) < 19 and graph[nx + dx[d]][ny + dy[d]] == num:
                    break

                # 육목이 아니면 출력
                print(num)
                print(x+1, y+1)
                return True
            nx += dx[d]
            ny += dy[d]

# 반복문을 빠져나가기 위한 값
IS_BREAK = False

# 완전탐색을 하면서 1이나 2일 때 check()를 돌려줌
for i in range(19):
    for j in range(19):
        if graph[i][j] == 1:
            if check(i, j, 1):
                IS_BREAK = True
                break
        if graph[i][j] == 2:
            if check(i, j, 2):
                IS_BREAK = True
                break
    if IS_BREAK:
        break
# 다 돌았는데 해당사항이 없으면 0 출력
else:
    print(0)