import heapq

n = int(input())
dasom = int(input())
candidate = [-int(input()) for _ in range(n-1)]
heapq.heapify(candidate)
cnt = 0

if candidate:
    while -candidate[0] >= dasom:
        heapq.heappush(candidate, heapq.heappop(candidate)+1)
        dasom += 1
        cnt += 1
    print(cnt)
else:
    print(0)