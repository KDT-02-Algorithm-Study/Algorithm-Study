# IF문 좀 대신 써줘 https://www.acmicpc.net/problem/19637
# 42036KB / 792ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = []
power = []

for i in range(n):
    tmp = input().split()
    # 중복으로 입력되는 전투력 제외
    if power and power[-1] == int(tmp[1]):
        continue
    name.append(tmp[0])
    power.append(int(tmp[1]))

for _ in range(m):
    now = int(input())
    # 탐색 구간을 power의 인덱스로 지정
    # 가장 왼쪽을 0, 가장 오른쪽을 마지막 인덱스로 두고 범위를 좁혀 나감
    s = 0
    e = len(power)
    ans = ''

    while s <= e:
        mid = int((s + e) / 2)
         
        # 현재 능력치가 기준 능력치(mid)보다 높으면 기준을 높여서 탐색
        if now > power[mid]:
            s = mid + 1
        else:
            # 낮으면 정답일 가능성이 있으므로 정답을 갱신하고 기준을 낮춰서 탐색
            ans = name[mid]
            e = mid - 1

    print(ans)