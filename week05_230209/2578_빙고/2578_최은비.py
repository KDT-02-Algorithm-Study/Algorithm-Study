# 빙고 https://www.acmicpc.net/problem/2578
 
import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)] # 입력으로 들어오는 빙고판
host = [list(map(int, input().split())) for _ in range(5)] # 사회자가 불러주는 수
board = {} # 좌표를 저장하기 위한 딕셔너리
check = [[0] * 5 for _ in range(5)] # 빙고판에서 사회자가 부른 수를 체크하기 위한 매트릭스
n = 0 # 사회자가 몇 번째 수를 불렀는가를 카운트할 변수
breaker = False # 빙고가 나오면 반복문을 나오기 위한 변수

for i in range(5):
    for j in range(5):
        # 내가 그린 빙고판에 어느 수가 어느 좌표에 표시되었는지를 딕셔너리에 저장
        # 수가 key, 좌표가 value
        board[bingo[i][j]] = (i, j)

# 사회자가 불러주는 수를 check 리스트에 표시
# 사회자가 부르지 않은 수는 0, 부른 수는 1
for i in range(5):
    for j in range(5):
        # 사회자가 부른 수의 좌표를 딕셔너리에 찾아서 저장
        r, c = board[host[i][j]]
        # 원래 0이었던 값을 1로 바꿈
        check[r][c] = 1
        # 사회자가 수를 부를 때마다 1씩 증가
        n += 1

        # 사회자가 최소 12번을 불러야 빙고 가능
        if n > 11:

            # check 리스트에서 가로로 빙고가 가능한지 확인
            res = 0
            for a in range(5):
                if sum(check[a]) == 5:
                    res += 1

            # 세로로 빙고가 가능한지 확인
            for a in range(5):
                cnt = 0
                for b in range(5):
                    if check[b][a] == 1:
                        cnt += 1

                if cnt == 5:
                    res += 1

            # (0, 4)에서 왼쪽 아래로 내려오는 대각선 확인
            cnt = 0
            for a in range(5):
                if check[a][5-a-1] == 1:
                    cnt += 1

                if cnt == 5:
                    res += 1

            # (0, 0)에서 오른쪽 위로 올라가는 대각선 확인
            cnt = 0
            for a in range(5):
                if check[a][a] == 1:
                    cnt += 1

                if cnt == 5:
                    res += 1

            # 빙고 수가 3개 이상이면 몇 번 불렀는지를 출력하고 반복문 종료
            if res > 2:
                print(n)
                breaker = True
                break

    if breaker:
        break