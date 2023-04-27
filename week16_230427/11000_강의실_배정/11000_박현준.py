# 68220 KB / 424 ms

import sys
import heapq
input = sys.stdin.readline
N = int(input())
lst = [[int(x) for x in input().split()] for _ in range(N)]
lst = sorted(lst)
# 강의실을 나타낼 힙큐
room = []
heapq.heappush(room, lst[0][1])

for i in range(1, N):
    
    # 현재 강의실
    cur_room = room[0]
    
    # 다음 수업의 시작시간과 종료시간을 next_start, next_end에 담는다
    next_start = lst[i][0]
    next_end = lst[i][1]
    
    # 다음 수업이 현재 수업중인 강의실의 종료시간보다 빠르면 이어서 사용
    if next_start < cur_room:
        heapq.heappush(room, next_end)
    
    # 아니면 강의실 추가
    else:
        heapq.heappop(room)
        heapq.heappush(room, next_end)
print(len(room))