# 강의실 배정 https://www.acmicpc.net/problem/11000
# 62076KB / 348ms
import sys
import heapq
input = sys.stdin.readline

n = int(input())
lecture = []
heap = [] # 끝나는 시간이 담긴 힙

for _ in range(n):
    a, b = map(int, input().split())
    lecture.append((a, b))

lecture = sorted(lecture)
heapq.heappush(heap, lecture[0][1])

for i in range(1, n):
    # heap: 현재 수업, lecture: 다음 수업
    # 현재 수업 종료 전에 다음 수업이 시작하면 강의실 하나 추가
    if lecture[i][0] < heap[0]:
        heapq.heappush(heap, lecture[i][1])
    # 현재 수업과 다음 수업이 겹치지 않으면 현재 수업은 빼고 다음 수업을 추가
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lecture[i][1])

print(len(heap))
