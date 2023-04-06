# 20055 컨베이어 벨트 위의 로봇
# 34160 KB / 3760 ms

from collections import deque

n, k = map(int, input().split())
A = list(map(int, input().split()))

robot_order = deque([]) # 로봇별 위치(선입선출)
robot_belt = [0]*n # 벨트위 로봇

cnt = 0
c = 0
while c < k:
    cnt += 1
    A = A[-1:]+A[:-1] # 벨트 이동
    l = len(robot_order)

    if robot_order: # 로봇이 있을 때
        for i in range(l): # 로봇의 갯수만큼
            a = robot_order.pop() # 먼저 들어온 순서대로 pop
            if a < n-2: # 
                if not robot_belt[a+2] and A[a+2] > 0:
                    robot_order.appendleft(a+2)
                    robot_belt[a], robot_belt[a+2] = 0, 1
                    A[a+2] -= 1
                    if A[a+2] == 0:
                        c += 1
                else:
                    robot_order.appendleft(a+1)
                    robot_belt[a], robot_belt[a+1] = 0, 1
            else:
                robot_belt[a] = 0

    if A[0] > 0:
        robot_order.appendleft(0)
        robot_belt[0] = 1
        A[0] -= 1
        if A[0] == 0:
            c += 1 
print(cnt)