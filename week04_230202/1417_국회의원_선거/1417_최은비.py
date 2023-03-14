# https://www.acmicpc.net/problem/1417

import sys
import heapq

input = sys.stdin.readline

n = int(input())
vote = [int(input()) for _ in range(n)]
ds = vote[0] # 다솜이 득표수 따로 저장
cnt = 0

if n == 1:
    print(0)
else:
    heap = []
    for num in vote:
        # 다솜이보다 낮은 득표는 필요 없어서 제외하고 heap에 저장
        # 높은 순으로 봐야하니까 최대힙으로 구현
        if num >= ds:
            heapq.heappush(heap, [-num, num])
    
    while heap:
        a = heapq.heappop(heap)
        
        # 0번째 요소를 뽑았을 때 heap이 비었다면 애초에 다솜이보다 높은 득표수가 없다는 뜻으로 표를 매수할 필요 X
        if not heap:
            break
        # 0번째 요소가 다솜이보다 작다면 heap에 다솜이보다 높은 득표수가 없다는 뜻으로 while문 나오기
        elif a[1] < ds:
            break
        # 아직 다솜이보다 높은 득표수가 남았다면 0번째 요소를 하나 빼주고 다시 heap에 push
        # 여기서 표를 하나 뺏었으니 다솜이 표에 +1
        else:
            a[1] -= 1
            a[0] = -a[1]
            heapq.heappush(heap, a)
            ds += 1
            cnt += 1

    print(cnt)