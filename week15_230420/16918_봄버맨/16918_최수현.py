# 31504 KB / 4088 ms
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

"""
0 폭탄1 심어짐
1 시간 지남
2 빈 곳에 폭탄2 심어짐
3 폭탄1 터짐
4 빈곳에 폭탄3 심어짐
5 폭탄2 터짐
.
.
"""

r, c, n = map(int, input().split())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [[0] * c for _ in range(r)]
# 0: 아무것도 없음, 1: 폭탄 설치, 2: 1초 지남, 3: 2초 지남, 4: 폭탄 터짐
for i in range(r):
    line = list(input().rstrip())
    for j in range(c):
        if line[j] == 'O':
            board[i][j] = 2
        else:
            board[i][j] = 0

# 1초 지난 것으로 시작하므로 -1
n -= 1
for t in range(n):
    # 모두 1초 증가(0인곳에 폭탄 심기 포함)
    for i in range(r):
        for j in range(c):
            board[i][j] += 1
    # 홀수일 경우 폭탄 터짐
    if t & 1:
        check = [[False] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] > 3:
                    check[i][j] = True
                    for dy, dx in delta:
                        ny = i + dy
                        nx = j + dx
                        if ny >= 0 and ny < r and nx >= 0 and nx < c:
                            if not check[ny][nx]:
                                check[ny][nx] = True
        for i in range(r):
            for j in range(c):
                if check[i][j]:
                    board[i][j] = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print()