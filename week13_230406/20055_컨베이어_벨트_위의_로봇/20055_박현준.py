# 34252 KB / 3228 ms

from collections import deque
N, K = map(int, input().split())
belt = deque([int(x) for x in input().split()])
robot = deque([0] * N)
cnt = 0

while True:
    cnt += 1
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 로봇이 존재하면 돌림
    if robot:
        # 돌림
        for i in range(N-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        # 마지막에 있는 로봇은 내림
        robot[-1] = 0

    # 로봇 올리기
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(cnt)