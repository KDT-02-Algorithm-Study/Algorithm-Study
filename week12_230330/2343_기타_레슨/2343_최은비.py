# 기타 레슨 https://www.acmicpc.net/problem/2343
# 42340KB / 480ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
video = list(map(int, input().split()))
# 모든 강의를 담을 수 있어야하므로 max를 사용
# 1 2 3 4 5 6 7 8 9일 때, 블루레이 크기가 8이면 9짜리 강의를 녹화하지 못함
s = max(video)
e = sum(video)
ans = 0

while s <= e:
    mid = (s + e) // 2 # 현재 블루레이 크기

    cnt = 1 # 필요한 블루레이 개수
    bluray = 0
    for i in range(n):
        bluray += video[i]

        if bluray > mid:
            cnt += 1
            # 녹화 가능한 용량보다 넘쳤으므로 방금 강의는 다음 블루레이에 녹화해야 함
            bluray = video[i]

    if cnt > m:
        s = mid + 1
    else:
        ans = mid
        e = mid - 1

print(ans)