# 봄버맨 https://www.acmicpc.net/problem/16918
# 34348KB / 3672ms
import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
tmp = deque()
# 봄버맨이 실제로 움직이기 시작하는 시간은 2초
time = 2

for i in range(r):
    for j in range(c):
        if board[i][j] == 'O':
            # 맨 처음 설치된 폭탄이 터지는 시간이 3초
            board[i][j] = 3

while time < n+1:

    if time % 2 != 0:
        for i in range(r):
            for j in range(c):
                # 현재 시간에 터지는 폭탄 좌표값을 모두 수집
                if board[i][j] == time:
                    tmp.append((i, j))
        # 범위에 들어오는 폭탄은 모두 터트리기
        while tmp:
            x, y = tmp.popleft()
            board[x][y] = '.'

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < r and 0 <= ny < c:
                    board[nx][ny] = '.'
    else:
        # 2초마다 폭탄이 설치되지 않은 모든 곳에 폭탄을 설치
        # 이때 설치된 폭탄은 3초 뒤에 터짐
        for i in range(r):
            for j in range(c):
                if board[i][j] == '.':
                    board[i][j] = time + 3

    time += 1
    

for i in range(r):
    for j in range(c):
        if board[i][j] != '.':
            print('O', end='')
        else:
            print('.', end='')
    print()



'''
# 31516KB / 68ms

import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
ans = [['O' for _ in range(c)] for _ in range(r)]

if n == 1:
    ans = board

elif n % 2 == 0:
    ans = [['O' for _ in range(c)] for _ in range(r)]

elif n % 4 == 3:
    # 초기 상태에서 설치된 폭탄만 터짐
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                ans[i][j] = '.'
                for dx, dy in dxy:
                    if 0 <= i+dx < r and 0 <= j+dy < c:
                        ans[i+dx][j+dy] = '.'

else:
    # 위 상태에서 한 단계 더 터트림
    tmp = [['O' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                ans[i][j] = '.'
                for dx, dy in dxy:
                    if 0 <= i+dx < r and 0 <= j+dy < c:
                        ans[i+dx][j+dy] = '.'

    for i in range(r):
        for j in range(c):
            if ans[i][j] == 'O':
                tmp[i][j] = '.'
                for dx, dy in dxy:
                    if 0 <= i+dx < r and 0 <= j+dy < c:
                        tmp[i+dx][j+dy] = '.'

    ans = tmp

for i in range(r):
    print(''.join(ans[i]))
'''
'''
0초: 초기상태
1초: 아무것도 X
2초: 모든 칸에 폭탄 설치
3초: 폭발
4초: 설치
5초: 폭발
...
'''