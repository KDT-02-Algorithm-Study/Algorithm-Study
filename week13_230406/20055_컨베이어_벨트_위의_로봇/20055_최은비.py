# 컨베이어 벨트 위의 로봇 https://www.acmicpc.net/problem/20055
# 31388KB / 3872ms
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * n
cnt = 0

while True:    
    # 1-1. 벨트 회전
    belt.insert(0, belt[-1])
    belt = belt[:len(belt)-1]

    # 1-2. 로봇 회전
    robot.insert(0, robot[-1])
    robot = robot[:len(robot)-1]
    # 내리는 위치에 있는 로봇 없애기
    if robot[-1] == 1:
        robot[-1] = 0

    # 2. 로봇 회전
    # 벨트에 먼저 올라간 로봇부터 -> 역순으로 탐색
    for i in range(len(robot)-1, -1, -1):
        # 2-1. 로봇이 이동하기 위한 조건
        if robot[i] == 1 and robot[i+1%n] == 0 and belt[i+1%n] > 0:
            robot[i] = 0 # 로봇을 현재 칸에서
            robot[i+1%n] = 1 # 다음 칸으로 이동
            belt[i+1%n] -= 1 # 벨트 내구도 감소

    # 내리는 위치면 로봇 없애기
    if robot[-1] == 1:
        robot[-1] = 0

    # 3. 올리는 위치에서 벨트 내구도가 0이 아니면 로봇 올리기
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    cnt += 1

    if belt.count(0) >= k:
        break

print(cnt)