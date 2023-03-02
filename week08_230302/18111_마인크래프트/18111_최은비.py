# 마인크래프트 https://www.acmicpc.net/problem/18111
# 31256KB, 140ms

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
# 딕셔너리에 땅 높이와 그 높이인 땅의 개수를 저장
ground = {}

for _ in range(n):
    for n in list(map(int, input().split())):
        if n not in ground:
            ground[n] = 1
        else:
            ground[n] += 1


max_h = max(ground.keys())
min_h = min(ground.keys())
res_t = int(1e9)
res_h = 0

# 가장 높은 높이와 낮은 높이 사이에서 적정 높이 찾기
for target in range(min_h, max_h+1):
    remove = 0
    build = 0
    item = b

    for h in ground:
        # 현재 땅 높이가 목표 땅 높이보다 낮으면 블럭 쌓기 수행
        # 쌓은 만큼 인벤토리에서 빼주기
        if target > h:
            build += ground[h] * (target - h)
            item -= ground[h] * (target - h)
        # 현재 땅 높이가 목표 땅 높이보다 높으면 블럭 제거 수행
        # 제거한 만큼 인벤토리에 추가
        elif target < h:
            remove += ground[h] * (h - target)
            item += ground[h] * (h - target)

    # 인벤토리가 음수면 적절한 높이가 아니므로 다음 반복문 수행
    if item < 0:
        break
    
    # 최저 시간과 그 때 땅 높이 저장(낮은 높이에서 시작하므로 무조건 최고 높이가 저장됨)
    if res_t >= remove * 2 + build:
        res_t = remove * 2 + build
        res_h = target

print(res_t, res_h)

