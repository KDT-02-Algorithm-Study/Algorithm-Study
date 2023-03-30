# 풍선 공장 https://www.acmicpc.net/problem/15810
# 143400KB / 2500ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = sorted(list(map(int, input().split())))
s = 1
# 가장 빨리 부는 사람이 m개를 불었을 때 걸리는 시간을 범위 끝으로 지정
e = min(time) * m
ans = 0

while s <= e:
    mid = int((s + e) / 2) # 주어진 시간
    tmp = 0 # mid 시간 동안 만들 수 있는 풍선 수 총합

    for i in time:
        tmp += mid // i

    # 현재 시간에서 만들 수 있는 풍선 수가 기준보다 적다면 시간을 늘려서 탐색
    if tmp < m:
        s = mid + 1
    else:
        # 정답일 가능성이 있으므로 정답으로 갱신하고 시간을 줄여서 탐색
        ans = mid
        e = mid - 1

print(ans)
