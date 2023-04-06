# 31388 KB / 44 ms
import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room = []

for _ in range(p):
    l, n = input().rstrip().split()
    l = int(l)

    for r in room:
        # 방이 차있는 경우
        if r:
            # 인원이 다 안차있고 레벨이 범위 내인 경우
            if len(r) < m and l >= r[0][0] - 10 and l <= r[0][0] + 10:
                # 현재 방에 추가 후 break
                r.append((l, n))
                break
    # 다 돌았는데 들어갈 방이 없으면 새로운 방 만들기
    else:
        room.append([(l, n)])

for i in range(len(room)):
    if len(room[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    for r in sorted(room[i], key=lambda x: x[1]):
        print(*r)