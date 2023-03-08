import sys

board = [sys.stdin.readline().split() for _ in range(5)]
x = [sys.stdin.readline().split() for _ in range(5)]
cnt = 0
binggo = 0

for i in range(5):
    for j in range(5):
        x_num = x[i][j]
        cnt += 1
        for a in range(5):
            for b in range(5):
                if board[a][b] == x_num:
                    board[a][b] = 'X'

        binggo = 0
        if cnt >= 12:
            for n in range(5):
                for m in range(5):
                    if board[n][m] != 'X':
                        break
                else:
                    binggo += 1

            for n in range(5):
                for m in range(5):
                    if board[m][n] != 'X':
                        break
                else:
                    binggo += 1

            n = m = 0
            for k in range(5):
                if board[n+k][m+k] != 'X':
                    break
            else:
                binggo += 1

            n = 5
            m = 0
            for k in range(5):
                if board[n-k-1][m+k] != 'X':
                    break
            else:
                binggo += 1

        if binggo >= 3:
            break
    if binggo >= 3:
            break

print(cnt)