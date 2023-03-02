# 트럭 https://www.acmicpc.net/problem/13335
# 31388KB, 92ms

import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = list(map(int, input().split())) # 트럭 정보
bridge = [0] * w # 다리에 올라가있는 트럭을 표시할 리스트
cnt = 0 # 건너는 데 걸리는 시간

while True:
    cnt += 1
    bridge.pop(0) # 시간이 지나면 트럭이 다리를 빠져나오니까 하나씩 빼주기

    # 건너올 트럭이 남았을 경우
    if truck: 
        # 다리에 있는 트럭과 다음 트럭의 무게를 더했을 때 다리 하중보다 크다면
        if sum(bridge) + truck[0] > l:
            # 다리에 트럭이 올라가면 안되니까 0을 삽입
            bridge.append(0)
        else:
            # 다리가 트럭 무게를 견딜 수 있으면 다음 트럭이 지나옴
            bridge.append(truck.pop(0))
    else: # 건너올 트럭은 없지만 다리에 트럭이 남았을 경우엔 0을 삽입
        bridge.append(0)
    
    # 다리에 더이상 트럭이 없다면 반복문 탈출
    if sum(bridge) == 0:
        break

print(cnt)

# deque 풀이
"""
n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
bridge = deque([0] * w)
idx = 0
cnt = 0

while True:
    bridge.popleft()

    if idx < n:
        tmp = truck[idx]

        if sum(bridge) + tmp <= l:
                bridge.append(tmp)
                idx += 1
        else:
            bridge.append(0)
    else:
         bridge.append(0)
    
    cnt += 1

    if sum(bridge) == 0:
        break

print(cnt)
"""