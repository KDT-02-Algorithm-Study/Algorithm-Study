# 톱니바퀴 https://www.acmicpc.net/problem/14891
# 34160KB / 68ms

import sys
from collections import deque
input = sys.stdin.readline

gear = [deque(list(map(int, input().strip()))) for _ in range(4)]
n = int(input())

for _ in range(n):
    num, d = map(int ,input().split())
    num -= 1
    # 다른 톱니 바퀴와 비교할 극을 저장
    left = gear[num][6]
    right = gear[num][2]

    # 입력으로 들어온 톱니바퀴 회전
    gear[num].rotate(d)

    now = d # 회전 방향
    # 왼쪽 톱니
    for i in range(num-1, -1, -1):
        if gear[i][2] != left: # 인접한 톱니 바퀴와 다른 극인 경우
            left = gear[i][6] # 비교할 극 갱신
            gear[i].rotate(now * -1)
            now *= -1 # 방향 바꿔주기
        else:
            # 같은 극이면 톱니바퀴가 회전하지 않으므로 반복문 탈출
            break

    now = d # 회전 방향
    # 오른쪽 톱니
    for i in range(num+1, 4):
        if gear[i][6] != right:
            right = gear[i][2]
            gear[i].rotate(now * -1)
            now *= -1
        else:
            break

ans = 0
for i in range(4):
    if gear[i][0] == 1:
        ans += (2 ** i)

print(ans)