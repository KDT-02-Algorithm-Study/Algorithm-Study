# 143400 KB, 1392 ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
staff = list(map(int, input().split()))

start = 1
# 가장 빠른 시간으로 풍선을 만드는 스태프가 m개를 다 만드는 시간
end = min(staff) * m
min_time = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum([mid // staff[i] for i in range(n)])

    # 최소 시간을 구해야 하므로 시간의 값을 큰 쪽에서 작은 쪽으로 줄임
    if cnt >= m:
        min_time = mid
        end = mid - 1
    else:
        start = mid + 1

print(min_time)