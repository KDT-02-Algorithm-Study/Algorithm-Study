# 18111 마인크래프트
# 34520 KB / 128 ms

import sys
sys.stdin = open('input_18111.txt', 'r')

import sys
from collections import Counter
input = sys.stdin.readline

n, m, b = map(int, input().split())
data = [] # 높이 data

# 1차원 리스트로 입력받기
for _ in range(n):
    data.extend(list(map(int,input().split()))) 
data = Counter(data) # 시간을 줄이기 위해 dict 형태로 바꿔준다.
cur_h = 0 # 현재 탐색하는 기준 높이

time = 0
ans_t = 1e9

# 직접 채우거나 깎으면서 탐색하면 시간을 알 수 없으므로
# 기준 높이마다 계속 확인한다.
while cur_h <= 256:
    cnt1 = cnt2 = 0

    # data 탐색
    for k, v in data.items():
        if k < cur_h:
            cnt1 += (cur_h-k) * v # 쌓아올리는 블럭 개수
        elif k > cur_h:
            cnt2 += (k-cur_h) * v # 깎는 블럭 개수
    
    if (b - cnt1 + cnt2) < 0: # 블럭 개수가 모자르면 컷
        break
    
    time = cnt1 + 2*cnt2 # 현재 높이 시간
    
    # 최소 시간 저장
    if time <= ans_t: 
        ans_t = time
        ans_h = cur_h

        cur_h += 1
    else:
        break
print(ans_t, ans_h)
