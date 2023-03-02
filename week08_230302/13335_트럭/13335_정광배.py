# 13335 트럭
# 34140 KB / 92 ms

import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
q = deque([0]*w) # 다리 정보를 담을 deque

i = 0 # 트럭의 index
time = 0
while i < n: 
    q.popleft() # 다리 앞쪽은 건너기 완료
    now = truck[i] # 대기중인 제일 앞 트럭 무게
    if sum(q) + now <= L: # 다리 위 트럭무게 + now 가 최대하중보다 작으면
        q.append(now) # 다음 트럭 입장~
        i += 1
    else:
        q.append(0)
    time += 1

while q:    # 다리 위 남아있는 트럭 보내기
    q.popleft()
    time += 1

print(time)