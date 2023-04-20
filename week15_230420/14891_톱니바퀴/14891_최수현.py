# 34176 KB / 72 ms
import sys
input = sys.stdin.readline
from collections import deque

wheel = [0] # index 0은 안씀
for _ in range(4):
    wheel.append(deque(input().rstrip()))

# 왼쪽 톱니=index 6 /오른쪽 톱니=index 2
k = int(input())
for _ in range(k):
    # 톱니바퀴 1, 2, 3, 4가 이번에 회전할 방향을 담을 리스트
    # 0번째 index는 안씀, -1 = 반시계방향 / 1 = 시계방향
    dir = [0] * 5
    n, d = map(int, input().split())
    dir[n] = d

    # 주어진 톱니바퀴의 왼쪽
    index = n - 1
    flag = wheel[n][6]
    while index > 0:
        if wheel[index][2] != flag:
            if dir[index+1] == 1:
                dir[index] = -1
            elif dir[index+1] == -1:
                dir[index] = 1
        flag = wheel[index][6]
        index -= 1

    # 주어진 톱니바퀴의 오른쪽
    index = n + 1
    flag = wheel[n][2]
    while index < 5:
        if wheel[index][6] != flag:
            if dir[index-1] == 1:
                dir[index] = -1
            elif dir[index-1] == -1:
                dir[index] = 1
        flag = wheel[index][2]
        index += 1

    # 저장된 방향대로 회전
    for i in range(1, 5):
        wheel[i].rotate(dir[i])

ans = 0
for i in range(1, 5):
    if wheel[i][0] == '1':
        ans += 2 ** (i-1)
print(ans)