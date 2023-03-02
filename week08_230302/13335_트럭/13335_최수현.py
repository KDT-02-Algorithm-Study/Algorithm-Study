# 메모리 34130 KB, 시간 76 ms
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
intput = sys.stdin.readline

n, length, wt = map(int, input().split())
truck = deque(map(int, input().split()))
# 다리를 지나간 트럭 저장
done = deque()
# 다리 위에 있는 트럭의 무게
on_bridge = 0
# 시간 카운트
cnt = 0

while truck:
    # 다리에 오른 트럭의 수가 다리길이-1 미만
    if len(done) < length - 1:
        # 다리 위에 있는 트럭과 올라갈 트럭의 합
        if on_bridge + truck[0] <= wt:
            x = truck.popleft()
            done.append(x)
            on_bridge += x
        else:
            done.append(0)

    # 다리에 오른 트럭의 수가 다리길이-1 미만
    else:
        if on_bridge + truck[0] <= wt:
            x = truck.popleft()
            done.append(x)
            # 올라올 트럭의 무게를 더하고 다리의 맨앞 트럭 무게 빼기(다음번에 나가니까)
            on_bridge = on_bridge + x - done.popleft()
        else:
            done.append(0)
            on_bridge -= done.popleft()
    cnt += 1

print(cnt + length)