# 나무 자르기 https://www.acmicpc.net/problem/2805
# 143400KB / 4412ms
import sys
input = sys.stdin.readline

n, target = map(int, input().split())
# 나무 높이가 중복된 경우가 있어서 시간이 오래 걸리는 듯...
tree = sorted(list(map(int, input().split())))
s = 1 # 자를 수 있는 최소 나무 길이
e = max(tree) # 자를 수 있는 최대 나무 길이
ans = 0

while s <= e:
    mid = int((s + e) / 2)
    tmp = 0 # 상근이가 가져갈 나무
    
    # 나무 높이가 저장된 리스트를 순회하면서 현재 기준값(mid)보다 큰 나무만 자름
    for i in tree:
        if i > mid:
            tmp += i - mid

    # 현재 가져갈 수 있는 나무가 목표 길이보다 작다면
    if tmp < target:
        # 자르는 높이를 높여서 다시 탐색
        e = mid - 1

    # 같거나 긴 경우
    else:
        # 정답으로 갱신하고 자르는 높이를 낮춰서 다시 탐색
        ans = mid
        s = mid + 1

print(ans)