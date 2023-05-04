# 빗물 https://www.acmicpc.net/problem/14719
# 31388KB / 44ms
import sys
input = sys.stdin.readline

c, r = map(int, input().split())
block = list(map(int, input().split()))
ans = 0
now = block[0]

for i in range(1, r-1):
    # 현재 블럭이 다음에 올 블럭보다 높으면 현재 블럭의 높이는 필요가 없음
    # 빗물이 담길 수 있는 최고 높이가 다음 블럭들 중에서 가장 높은 높이가 됨
    if now > max(block[i:]):
        now = max(block[i:])

    # 현재 블럭(now) 높이가 다음 블럭(block[i]) 높이보다 높으면
    # 두 블럭의 차이만큼 빗물이 담길 수 있음
    if block[i] < now:
        ans += now - block[i]
    # 현재 블럭 높이가 다음 블럭보다 낮으면 빗물이 담길 수 없음
    else:
        now = block[i]

print(ans)