import sys
input = sys.stdin.readline
from collections import deque

def jump(b, a):
    q = deque([(b, a)])

    while q:
        y, x = q.popleft()
        if matrix[y][x] == -1:
            return print('HaruHaru')
        elif matrix[y][x] == 0:
            continue
        else:
            v = matrix[y][x]
            matrix[y][x] = 0
            if 0 <= y+v < n:
                q.append((y+v, x))
            if 0 <= x+v < n:
                q.append((y, x+v))
    else:
        return print('Hing')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
jump(0, 0)