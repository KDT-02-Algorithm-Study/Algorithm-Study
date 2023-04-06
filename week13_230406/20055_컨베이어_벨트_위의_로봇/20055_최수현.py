# 34144 KB / 3029 ms
import sys
input = sys.stdin.readline
from collections import deque

n, k= map(int, input().split())
# 벨트의 내구성
belt = deque(map(int, input().split()))
# 로봇의 위치
robots = deque([False] * 2 * n)
# 몇 단계인지 카운트
turn = 0

while k > 0:
    turn += 1
    # 컨베이어벨트 한칸 이동
    belt.appendleft(belt.pop())
    robots.appendleft(robots.pop())
    # n번째에 있는 로봇 내림
    robots[n-1] = False

    for i in reversed(range(n-1)):
        # 앞에 로봇이 없고 내구성 0 이상인 경우
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1
            # 내구성 0이면 k - 1
            if belt[i+1] == 0:
                k -= 1
    
    # n번째에 있는 로봇 내림
    robots[n-1] = False

    # 1번 칸 내구성이 0이상이면 로봇 올리기
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
        # 내구성 0이면 k - 1
        if belt[0] == 0:
            k -= 1

print(turn)