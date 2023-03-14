from collections import deque
import sys

n = int(input())
orders = list(sys.stdin.readline().rstrip())
way = deque(['d', 'r', 'u', 'l'])
x = y = 0
x_track = [0]
y_track = [0]

for order in orders:
    if order == 'F':
        if way[0] == 'd':
            y -= 1
        elif way[0] == 'r':
            x += 1
        elif way[0] == 'u':
            y += 1
        else:
            x -= 1
        x_track.append(x)
        y_track.append(y)
    else:
        if order == 'R':
            way.appendleft(way.pop())
        elif order == 'L':
            way.append(way.popleft())

max_x = max(x_track)
min_x = min(x_track)
min_y = min(y_track)
maze = [['#']*(max_x-min_x+1) for _ in range(max(y_track)-min_y+1)]

for i in range(len(x_track)):
    maze[y_track[i]-min_y][x_track[i]-min_x] = '.'

for m in maze[::-1]:
    print(''.join(m))
