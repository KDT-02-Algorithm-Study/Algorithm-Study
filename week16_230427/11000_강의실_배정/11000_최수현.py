# 73584 KB / 388 ms
import sys
input = sys.stdin.readline
import heapq

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()  # 시작시간, 끝나는 시간 순서로 정렬
classes = [time[0][1]] # index 0의 끝나는 시간을 넣고 시작

for i in range(1, n):
    # 시작시간은 비교하는 용도, 끝나는 시간은 리스트에 push
    s, e = time[i]
    if classes[0] > s:
        heapq.heappush(classes, e)
    else:
        # replace == poppush
        heapq.heapreplace(classes, e)

print(len(classes))