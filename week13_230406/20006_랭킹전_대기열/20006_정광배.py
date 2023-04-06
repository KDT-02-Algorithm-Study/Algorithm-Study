# 20006 랭킹전 대기열
# 31256 KB / 40 ms

import sys
input = sys.stdin.readline

p, m = map(int, input().split()) # 플레이어의 수, 방의 정원
rooms = []

for _ in range(p):
    now = input().rstrip().split() # [레벨, 닉네임]
    flag = 0 # flag
    now[0] = int(now[0])
    for room in rooms:
        if len(room) == m: # 이미 풀방이면 다음 방 탐색
            continue
        if room[0][0]-10 <= now[0] <= room[0][0]+10: # 방장의 레벨과 now의 레벨 비교
            room.append(now)
            flag = 1 
            break
    if not flag: # 방에 못 들어갔으면 새 방 만들기
        rooms.append([now])

# 방을 돌아가며 출력
for room in rooms: 
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room_ = sorted(room, key=lambda x: x[1]) # 닉네임 사전순 정렬
    for player in room_:
        print(' '.join(map(str,player)))

'''
[
    [[10, 'a'], [20, 'c'], [15, 'b'], [17, 'f'], [18, 'g']], 
    [[25, 'd'], [30, 'e'], [26, 'h'], [24, 'i'], [28, 'j']]
]
'''